#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	Net
%define		pnam	Twitter
%include	/usr/lib/rpm/macros.perl
Summary:	Net::Twitter - A perl interface to the Twitter API
Name:		perl-Net-Twitter
Version:	3.18001
Release:	0.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Net/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	88665d245f72b48ee87817edb5906d00
URL:		http://search.cpan.org/dist/Net-Twitter/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Crypt-SSLeay >= 0.5
BuildRequires:	perl-Data-Visitor
BuildRequires:	perl-DateTime >= 0.51
BuildRequires:	perl-DateTime-Format-Strptime >= 1.09
BuildRequires:	perl-Devel-StackTrace >= 1.21
BuildRequires:	perl-Digest-HMAC
BuildRequires:	perl-HTML-Parser
BuildRequires:	perl-HTTP-Message
BuildRequires:	perl-JSON
BuildRequires:	perl-Moose >= 0.9
BuildRequires:	perl-Moose-Exporter
BuildRequires:	perl-Moose-Role
BuildRequires:	perl-MooseX-Aliases
BuildRequires:	perl-MooseX-Role-Parameterized
BuildRequires:	perl-Net-OAuth >= 0.25
BuildRequires:	perl-Test-Fatal
BuildRequires:	perl-Try-Tiny >= 0.03
BuildRequires:	perl-URI >= 1.4
BuildRequires:	perl-libwww >= 2.032
BuildRequires:	perl-namespace-autoclean >= 0.09
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a Perl interface to the Twitter APIs. See
<http://dev.twitter.com/doc> for a full description of the Twitter
APIs.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/Net/Twitter.pod

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Net/*.pm
%{perl_vendorlib}/Net/Twitter
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
