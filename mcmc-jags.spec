#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries
#
Summary:	Just Another Gibbs Sample
Name:		mcmc-jags
Version:	3.3.0
Release:	1
License:	GPL v2
Group:		Development/Libraries
Source0:	http://downloads.sourceforge.net/mcmc-jags/JAGS/3.x/Source/JAGS-%{version}.tar.gz
# Source0-md5:	1fdcf7d3c38ea418198d180d0f150545
URL:		http://mcmc-jags.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JAGS is Just Another Gibbs Sampler - a program for analysis of Bayesian
hierarchical models using Markov Chain Monte Carlo (MCMC) simulation not
wholly unlike BUGS.

%package devel
Summary:	Header files for JAGS library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for JAGS library.

%package static
Summary:	Static JAGS library
Summary(pl.UTF-8):	Statyczna biblioteka quvi
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static JAGS library.

%prep
%setup -q -n JAGS-%{version}

%build
%configure \
	%{?with_static_libs:--enable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/jags
%attr(755,root,root) %{_libdir}/jags-terminal
%attr(755,root,root) %{_libdir}/libjags.so.*.*.*
%attr(755,root,root) %{_libdir}/libjrmath.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libjags.so.3
%attr(755,root,root) %ghost %{_libdir}/libjrmath.so.0

%dir %{_libdir}/JAGS
%dir %{_libdir}/JAGS/modules-3
%attr(755,root,root) %{_libdir}/JAGS/modules-3/*.so
%{_libdir}/JAGS/modules-3/*.la

%{_mandir}/man1/*.1*

%files devel
%defattr(644,root,root,755)
#%doc doc/*
%attr(755,root,root) %{_libdir}/libjags.so
%attr(755,root,root) %{_libdir}/libjrmath.so
%{_includedir}/JAGS
%{_pkgconfigdir}/jags.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libjags.a
%{_libdir}/libjrmath.a
%endif
