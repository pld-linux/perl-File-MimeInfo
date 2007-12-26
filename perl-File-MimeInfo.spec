#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	File
%define	pnam	MimeInfo
Summary:	File::MimeInfo - use the freedesktop mimeinfo spec
Summary(pl.UTF-8):	File::MimeInfo - używanie specyfikacji mimeinfo z freedesktop
Name:		perl-File-MimeInfo
Version:	0.14
Release:	0.1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/File/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b4cb0ea1a30730c24747199784d90968
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

%description -l pl.UTF-8
Ten moduł może być używany do okreslenia typu MIME danego pliku; jest
zamiennikiem File::MMagic próbującym implementować specyfikację
freedesktop do używania współdzielonej bazy danych mime-info. Ten
pakiet zawiera skrypt mimetype, który może być używany jako
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
%attr(755,root,root) %{_bindir}/mimeopen
%{perl_vendorlib}/File/*.pm
%dir %{perl_vendorlib}/File/MimeInfo
%{perl_vendorlib}/File/MimeInfo/*.pm
%{_mandir}/man1/*
%{_mandir}/man3/*
