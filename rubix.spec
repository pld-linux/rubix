Summary:	Rubik's cube simulation
Summary(pl.UTF-8):	Symulacja kostki Rubika
Name:		rubix
Version:	1.0.5
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://sed.free.fr/rubix/%{name}-%{version}.tar.bz2
# Source0-md5:	cb5c672eb9dd6286c292d0408dbec26d
Patch0:		%{name}-Makefile.patch
URL:		http://sed.free.fr/rubix/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
rubix is a Rubik's cube simulation for the Linux operating system.

%description -l pl.UTF-8
rubix jest symulacją kostki Rubika dla systemów Linux.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	OPTFLAGS="%{rpmcflags}" \
	GAMESDIR="%{_bindir}"

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