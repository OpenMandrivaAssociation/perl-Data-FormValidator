%define upstream_name    Data-FormValidator
%define upstream_version 4.66

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Validates user input based on input profile
License:    Artistic/GPL
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Data/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Date::Calc)
BuildRequires:  perl(File::MMagic)
BuildRequires:  perl(Image::Size)
BuildRequires:  perl(Regexp::Common)
BuildRequires:  perl(CGI)
BuildRequires:  perl(MIME::Types)
BuildRequires:  perl(Perl6::Junction)
BuildRequires:  perl(Email::Valid)
BuildArch:      noarch
Buildroot:      %{_tmppath}/%{name}-%{version}-%{release}

%description
Data::FormValidator's main aim is to make input validation expressible in a
simple format. Data::FormValidator lets you define profiles which declare the
required and optional fields and any constraints they might have.

The results are provided as an object which makes it easy to handle missing and
invalid results, return error messages about which constraints failed, or
process the resulting valid data.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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


