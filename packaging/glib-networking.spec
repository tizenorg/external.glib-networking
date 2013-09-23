Name:       glib-networking
Summary:    Network extensions for GLib
Version:    2.32.3_1.4
Release:    1
Group:      System/Libraries
License:    LGPLv2
URL:        http://git.gnome.org/browse/glib-networking/
Source0:    http://ftp.gnome.org/pub/gnome/sources/%{name}/2.32/%{name}-%{version}.tar.xz

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  intltool
BuildRequires:  ca-certificates

%description
Networking extensions for GLib



%prep
%setup -q -n %{name}-%{version}

%build

%configure --disable-static --without-ca-certificates
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/license
cp COPYING %{buildroot}/usr/share/license/%{name}

%make_install

%find_lang glib-networking

%files
%manifest glib-networking.manifest

%files -f glib-networking.lang
%defattr(-,root,root,-)
%{_libdir}/gio/modules/libgiognutls.so
/usr/share/license/%{name}

%changelog
* Mon Sep 23 2013 Keunsoon Lee <keunsoon.lee@samsung.com>
- [Release] Update changelog for glib-networking-2.32.3_1.4

* Thu Nov 22 2012 praveen.ks <praveen.ks@samsung.com>
- [Release] Update changelog for glib-networking-2.32.3_1.3

