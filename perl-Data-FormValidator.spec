%define module  Data-FormValidator
%define name    perl-%{module}
%define version 4.50
%define release %mkrel 1

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Validates user input based on input profile
License:        Artistic/GPL
Group:          Development/Perl
URL:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Data/%{module}-%{version}.tar.bz2
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Date::Calc)
BuildRequires:  perl(File::MMagic)
BuildRequires:  perl(Image::Size)
BuildRequires:  perl(Regexp::Common)
BuildRequires:  perl(CGI)
BuildRequires:  perl(MIME::Types)
BuildArch:      noarch
Buildroot:      %{_tmppath}/%{name}-%{version}

%description
Data::FormValidator's main aim is to make input validation expressible in a
simple format. Data::FormValidator lets you define profiles which declare the
required and optional fields and any constraints they might have.

The results are provided as an object which makes it easy to handle missing and
invalid results, return error messages about which constraints failed, or
process the resulting valid data.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%install
%{__rm} -rf %{buildroot}
./Build install destdir=%buildroot

%files
%defattr(-,root,root)
%doc README RELEASE_NOTES
%{perl_vendorlib}/Data
%{_mandir}/*/*

%clean
rm -rf %{buildroot}


