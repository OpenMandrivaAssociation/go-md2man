%define debug_package %nil

%define import_path github.com/cpuguy83/go-md2man
%define gopath %{_libdir}/go
%define gosrc %{gopath}/src/%{import_path}

Summary:	Transform md into man pages
Name:		go-md2man
Version:	1.0.2
Release:	3
License:	Specific
Group:		Development/Other
Url:		https://%{import_path}
Source0:        https://%{import_path}/archive/v%{version}.tar.gz
Provides:       golang(%{import_path}) = %{version}-%{release}
Provides:       golang(%{import_path}/mangen)
BuildRequires:	golang-blackfriday-devel
BuildRequires:	golang-net-devel

%package devel
BuildRequires:  golang >= 1.3.3
#BuildRequires:  golang-blackfriday-devel
#BuildRequires:  golang-net-devel
Requires:       golang >= 1.3.3
Summary:        Transform md into man pages devel part

%description
Transform md into man pages

%description devel
Transform md into man pages devel part

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
for d in . mangen; do
    install -d -p %{buildroot}/%{gosrc}/$d
    cp -av $d/*.go %{buildroot}/%{gosrc}/$d
done
rm -f %{buildroot}%{gosrc}/{README.md}
pwd
install -d -m 755 %{buildroot}/%{_bindir}
install -m 755 %{name} %{buildroot}/%{_bindir}/%{name}

%files
%doc README.md
%{_bindir}/%{name}

%files devel
%doc README.md
%dir %attr(755,root,root) %{gosrc}
%dir %attr(755,root,root) %{gosrc}/mangen
%{gosrc}/*.go
%{gosrc}/*/*.go


