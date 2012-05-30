%define keepstatic 1

Name:       glib-networking
Summary:    Network extensions for GLib
Version:    2.28.7
Release:    1
Group:      System/Libraries
License:    LGPLv2
URL:        http://git.gnome.org/browse/glib-networking/
Source0:    http://ftp.gnome.org/pub/gnome/sources/%{name}/2.28/%{name}-%{version}.tar.bz2
Source1001: packaging/glib-networking.manifest 
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  intltool
BuildRequires:  ca-certificates


%description
Networking extensions for GLib



%prep
%setup -q -n %{name}-%{version}


%build
cp %{SOURCE1001} .

%configure --disable-static \
  --with-ca-certificates=/opt/etc/ssl/certs
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

%find_lang glib-networking






%files -f glib-networking.lang
%manifest glib-networking.manifest
%defattr(-,root,root,-)
%{_libdir}/gio/modules/libgiognutls.so


