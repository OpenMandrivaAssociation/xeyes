Name:		xeyes
Version:	1.2.0
Release:	2
Summary:	A follow the mouse X demo
Group:		Development/X11
Source:		http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT

BuildRequires:	pkgconfig(x11) >= 1.0.0
BuildRequires:	pkgconfig(xext) >= 1.0.0
BuildRequires:	pkgconfig(xi)
BuildRequires:	pkgconfig(xmu) >= 1.0.0
BuildRequires:	pkgconfig(xt) >= 1.0.0
BuildRequires:	pkgconfig(xrender) >= 0.4
BuildRequires:	x11-util-macros >= 1.0.1

%description
xeyes is a graphical computer program showing two googly eyes which
follow the cursor movements on the screen as if they were watching it.

%prep
%autosetup -n %{name}-%{version} -p1

%build
%configure \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make_build

%install
%make_install

%files
%{_bindir}/xeyes
%{_mandir}/man1/xeyes.1*
