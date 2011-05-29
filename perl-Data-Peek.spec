%define upstream_name    Data-Peek
%define upstream_version 0.31

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 3

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
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc META.yml ChangeLog README
%{_mandir}/man3/*
%perl_vendorlib/*


