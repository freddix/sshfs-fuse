Summary:	Filesystem based on the SSH File Transfer Protocol
Name:		sshfs-fuse
Version:	2.2
Release:	13
License:	GPL v2
Group:		Applications/System
Source0:	http://downloads.sourceforge.net/project/fuse/sshfs-fuse/2.2/%{name}-%{version}.tar.gz
# Source0-md5:	26e9206eb5169e87e6f95f54bc005a4f
URL:		http://fuse.sourceforge.net/
BuildRequires:	fuse-devel
BuildRequires:	glib-devel
BuildRequires:	pkg-config
Requires:	fuse
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Filesystem based on the SSH File Transfer Protocol.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/sshfs
%{_mandir}/man1/sshfs.1.*

