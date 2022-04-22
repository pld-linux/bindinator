Summary:	Tool to generate C# binding project
Summary(pl.UTF-8):	Narzędzie do generowania projektu z wiązaniami C#
Name:		bindinator
Version:	1.0
%define	gitref	c29b965e5ee4a9bd7fcf6b8f4d78dba6c9cbe6ac
%define	snap	20201020
Release:	0.%{snap}.1
License:	MIT
Group:		Development/Tools
Source0:	https://github.com/GLibSharp/bindinator/archive/%{gitref}/%{name}-%{snap}.tar.gz
# Source0-md5:	940e8b3f838000e7b428f01a7e47dec0
URL:		https://github.com/GLibSharp/bindinator
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
# gapi3-fixup
BuildRequires:	dotnet-gtk-sharp3-devel
BuildRequires:	gobject-introspection-devel
# uuidgen
BuildRequires:	libuuid
BuildRequires:	libxml2-progs
BuildRequires:	libxslt-progs
BuildRequires:	pkgconfig
BuildRequires:	unix2dos
Requires:	dotnet-gtk-sharp3-devel
Requires:	libuuid
Requires:	libxml2-progs
Requires:	libxslt-progs
Requires:	pkgconfig
Requires:	unix2dos
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The bindinator installs a tool called bindinate, which can be called
with the name of a gir file to generate a C# binding project.

%description -l pl.UTF-8
Pakiet bindinator zawiera narzędzie o nazwie bindinate, które po
wywołaniu z nazwą pliku gir generuje projekt z wiązaniami C#.

%prep
%setup -q -n %{name}-%{gitref}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
%if "%{_host_cpu}" != "x32"
	--host=%{_host} \
	--build=%{_host}
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS LICENSE README.md
%attr(755,root,root) %{_bindir}/bindinate
%{_prefix}/lib/bindinator
