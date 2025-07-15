Summary:	Rubik's cube simulation
Summary(pl.UTF-8):	Symulacja kostki Rubika
Name:		rubix
Version:	1.0.6
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://sed.free.fr/rubix/%{name}-%{version}.tar.bz2
# Source0-md5:	76346b49b67dd7ade0f69b4ae77e3f3a
Patch0:		%{name}-Makefile.patch
URL:		http://sed.free.fr/rubix/
BuildRequires:	xorg-lib-libX11-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
rubix is a Rubik's cube simulation for the Linux operating system.

%description -l pl.UTF-8
rubix jest symulacją kostki Rubika dla systemów Linux.

%prep
%setup -q
%patch -P0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	OPTFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}" \
	GAMESDIR="%{_bindir}" \
	XINC= \
	XLIB=-lX11

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install rubix $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS README TODO
%attr(755,root,root) %{_bindir}/%{name}
