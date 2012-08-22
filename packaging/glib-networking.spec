#sbs-git:slp/pkgs/g/glib-networking glib-networking 2.28.7 25dc079cae5b976413638d810f4ba2dc49abb59f
%define keepstatic 1

Name:       glib-networking
Summary:    Network extensions for GLib
Version: 2.28.7
Release:    1
Group:      System/Libraries
License:    LGPLv2
URL:        http://git.gnome.org/browse/glib-networking/
Source0:    http://ftp.gnome.org/pub/gnome/sources/%{name}/2.28/%{name}-%{version}.tar.gz
Patch1: 01_tls_small_keys.patch
Patch2: 02_gerror_crash.patch
Patch3: 03_tls_compat.patch
Patch4: 04_rehandshake.patch
Patch5: 05_virtualhosts.patch
Patch6: 06_gnutls3.patch

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  intltool
BuildRequires:  ca-certificates


%description
Networking extensions for GLib



%prep
%setup -q -n %{name}-%{version}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build

%configure --disable-static \
  --with-ca-certificates=/opt/etc/ssl/certs
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

%find_lang glib-networking






%files -f glib-networking.lang
%defattr(-,root,root,-)
%{_libdir}/gio/modules/libgiognutls.so


