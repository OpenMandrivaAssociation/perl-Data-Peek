%define upstream_name    Data-Peek%define upstream_version 0.40

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	3

Summary:    A collection of low-level debug facilities
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Data/%{upstream_name}-%{upstream_version}.tgz

BuildRequires: perl(Data::Dumper)
BuildRequires: perl(DynaLoader)
BuildRequires: perl(Test::Harness)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::NoWarnings)
BuildRequires: perl-devel

%description
Data::Peek started off as 'DDumper' being a wrapper module over the
Data::Dumper manpage, but grew out to be a set of low-level data
introspection utilities that no other module provided yet, using the lowest
level of the perl internals API as possible.

DDumper ($var, ...)
    Not liking the default output of Data::Dumper, and always feeling the
    need to set '$Data::Dumper::Sortkeys = 1;', and not liking any of the
    default layouts, this function is just a wrapper around
    Data::Dumper::Dumper with everything set as I like it.

        $Data::Dumper::Sortkeys = 1;
        $Data::Dumper::Indent   = 1;

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
yes | %{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%clean

%files
%doc META.yml ChangeLog README
%{_mandir}/man3/*
%perl_vendorlib/*




%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.310.0-4
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Sun May 29 2011 Funda Wang <fwang@mandriva.org> 0.310.0-3
+ Revision: 681379
- mass rebuild

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.310.0-2mdv2011.0
+ Revision: 555771
- rebuild for perl 5.12

* Tue Mar 16 2010 Jérôme Quelin <jquelin@mandriva.org> 0.310.0-1mdv2010.1
+ Revision: 521760
- import perl-Data-Peek


* Tue Mar 16 2010 cpan2dist 0.31-1mdv
- initial mdv release, generated with cpan2dist


