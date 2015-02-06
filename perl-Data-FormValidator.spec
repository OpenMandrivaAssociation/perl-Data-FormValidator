%define upstream_name    Data-FormValidator
%define upstream_version 4.81

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    3

Summary:    Validates user input based on input profile
License:    Artistic/GPL
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Data/Data-FormValidator-%{upstream_version}.tar.gz

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
./Build install destdir=%buildroot

%files
%doc  RELEASE_NOTES
%{perl_vendorlib}/Data
%{_mandir}/*/*

%clean




%changelog
* Sun May 29 2011 Funda Wang <fwang@mandriva.org> 4.660.0-2mdv2011.0
+ Revision: 681374
- mass rebuild

* Thu Feb 25 2010 Jérôme Quelin <jquelin@mandriva.org> 4.660.0-1mdv2011.0
+ Revision: 510969
- update to 4.66

* Thu Dec 31 2009 Jérôme Quelin <jquelin@mandriva.org> 4.650.0-1mdv2010.1
+ Revision: 484372
- update to 4.65

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 4.630.0-1mdv2010.0
+ Revision: 406970
- rebuild using %%perl_convert_version

* Sun Jan 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 4.63-1mdv2009.1
+ Revision: 324492
- update to new version 4.63

* Tue Jun 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 4.61-1mdv2009.0
+ Revision: 223407
- update to new version 4.61

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Nov 07 2007 Guillaume Rousse <guillomovitch@mandriva.org> 4.57-1mdv2008.1
+ Revision: 106645
- update to new version 4.57
- update to new version 4.57

* Thu Nov 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 4.56-1mdv2008.1
+ Revision: 104519
- update to new version 4.56

* Mon Aug 06 2007 Olivier Thauvin <nanardon@mandriva.org> 4.51-1mdv2008.0
+ Revision: 59255
- 4.51


* Sat Dec 09 2006 Olivier Thauvin <nanardon@mandriva.org> 4.50-1mdv2007.0
+ Revision: 93913
- 4.50
- buidrequires
- bump release to please upload system
- fix buildrequires
- 4.40
- Import perl-Data-FormValidator

* Thu Aug 03 2006 Guillaume Rousse <guillomovitch@mandriva.org> 4.30-1mdv2007.0
- New version 4.30

* Fri Jun 16 2006 Guillaume Rousse <guillomovitch@mandriva.org> 4.20-1mdv2007.0
- new version
- spec cleanup
- rpmbuildupdate aware

* Sat Mar 25 2006 Nicolas Lécureuil <neoclust@mandriva.org> 4.14-2mdk
- Add BuildRequires

* Fri Mar 24 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 4.14-1mdk
- First Mandriva release


