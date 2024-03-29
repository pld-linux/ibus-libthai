Summary:	Thai input method engine for IBus
Summary(pl.UTF-8):	Silnik metody wprowadzania znaków tajskich dla platformy IBus
Name:		ibus-libthai
Version:	0.1.5
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	https://linux.thai.net/pub/thailinux/software/libthai/%{name}-%{version}.tar.xz
# Source0-md5:	029f0c7ad8ab946eb878f24f1527aa53
URL:		https://linux.thai.net/
BuildRequires:	gettext-tools >= 0.18.1
BuildRequires:	glib2-devel >= 1:2.26.0
BuildRequires:	gtk+3-devel >= 3.16
BuildRequires:	ibus-devel >= 1.3.0
BuildRequires:	libthai-devel >= 0.1.19
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.596
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	glib2 >= 1:2.26.0
Requires:	gtk+3 >= 3.16
Requires:	libthai >= 0.1.19
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/ibus

%description
IBus-LibThai is a Thai input method engine for IBus, based on the
LibThai library.

Currently, it provides 3 keyboard layouts internally:
 - Ketmanee
 - Pattachote
 - TIS-820.2538
(Thai XKB symbols are also supported.)

%description -l pl.UTF-8
IBus-LibThai to silnik metody wprowadzania znaków tajskich dla
platformy IBus, oparty na bibliotece LibThai.

Obecnie udostępnia wewnętrznie 3 układy klawiatury:
 - Metmanee
 - Pattachote
 - TIS-820.2538
(tajskie symbole XKB są także obsługiwane).

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas

%postun
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libexecdir}/ibus-engine-libthai
%attr(755,root,root) %{_libexecdir}/ibus-setup-libthai
%{_datadir}/glib-2.0/schemas/org.freedesktop.ibus.libthai.gschema.xml
%{_datadir}/ibus-libthai
%{_datadir}/ibus/component/libthai.xml
