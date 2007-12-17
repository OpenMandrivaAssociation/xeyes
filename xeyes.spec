Name:		xeyes
Version:	1.0.1
Release:	%mkrel 4
Summary:	A follow the mouse X demo
Group:		Development/X11
Source:		http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT

BuildRequires:	libx11-devel >= 1.0.0
BuildRequires:	libxext-devel >= 1.0.0
BuildRequires:	libxmu-devel >= 1.0.0
BuildRequires:	libxt-devel >= 1.0.0
BuildRequires:	x11-util-macros >= 1.0.1

%description
xeyes is a graphical computer program showing two googly eyes which
follow the cursor movements on the screen as if they were watching it.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/xeyes
%{_mandir}/man1/xeyes.1x*

