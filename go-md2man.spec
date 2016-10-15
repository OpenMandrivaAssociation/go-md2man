%define debug_package %nil

%define import_path github.com/cpuguy83/go-md2man
%define gopath %{_libdir}/go
%define gosrc %{gopath}/src/%{import_path}

Summary:	Transform md into man pages
Name:		go-md2man
Version:	1.0.6
Release:	1
License:	Specific
Group:		Development/Other
Url:		https://%{import_path}
Source0:        https://%{import_path}/archive/v%{version}.tar.gz
Provides:       golang(%{import_path}) = %{version}-%{release}
Provides:       golang(%{import_path}/mangen)
BuildRequires:	golang-blackfriday-devel
BuildRequires:	golang-net-devel

%description
Transform md into man pages

%prep
%setup -q  -n %{name}-%{version}

%build
go env
mkdir -p ./_build/src/github.com/cpuguy83/
ln -s $(pwd) ./_build/src/%{import_path}
export GOPATH=$(pwd)/_build:%{gopath}
pushd $(pwd)/_build/src/%{import_path}
go build
popd

%install
mkdir -p %{buildroot}%{gosrc}
rm -f %{buildroot}%{gosrc}/{README.md}
install -d -m 755 %{buildroot}/%{_bindir}
install -m 755 %{name} %{buildroot}/%{_bindir}/%{name}
# generate man page
install -d -p %{buildroot}%{_mandir}/man1
./go-md2man -in=go-md2man.1.md -out=go-md2man.1
install -p -m 644 go-md2man.1 %{buildroot}%{_mandir}/man1

%files
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.*
