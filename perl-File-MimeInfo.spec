#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	File
%define	pnam	MimeInfo
Summary:	File::MimeInfo - use the freedesktop mimeinfo spec
Summary(pl):	File::MimeInfo - u¿ywanie specyfikacji mimeinfo z freedesktop
Name:		perl-File-MimeInfo
Version:	0.10
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	79c8d21705ce9d86a415275b8b2e6c52
URL:		http://search.cpan.org/dist/File-MimeInfo/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-File-BaseDir
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	shared-mime-info
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module can be used to determine the MIME type of a file; it's a
replacement for File::MMagic trying to implement the freedesktop
specification for using the shared mime-info database. The package
comes with a script called 'mimetype' that can be used as a file(1)
work-alike.

%description -l pl
Ten modu³ mo¿e byæ u¿ywany do okreslenia typu MIME danego pliku; jest
zamiennikiem File::MMagic próbuj±cym implementowaæ specyfikacjê
freedesktop do u¿ywania wspó³dzielonej bazy danych mime-info. Ten
pakiet zawiera skrypt mimetype, który mo¿e byæ u¿ywany jako
odpowiednik file(1).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mimetype
%{perl_vendorlib}/File/*.pm
%dir %{perl_vendorlib}/File/MimeInfo
%{perl_vendorlib}/File/MimeInfo/*.pm
%{_mandir}/man1/*
%{_mandir}/man3/*
