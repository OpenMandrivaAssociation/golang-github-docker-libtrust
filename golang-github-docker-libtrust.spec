%global debug_package   %{nil}
%global provider_tld    com
%global provider        github
%global project         docker
%global repo            libtrust
%global import_path     %{provider}.%{provider_tld}/%{project}/%{repo}
%global commit          d273ef2565cab2fd9832b8a3d6320e5ab39ef9db
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0
Release:        0.2.git%{shortcommit}
Summary:        Library for managing authentication and authorization
License:        ASL 2.0
URL:            https://%{import_path}
Source0:        https://%{import_path}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz
BuildArch:      noarch

%description
%{summary}.

Authentication is handled using the identity attached
to the public key. Libtrust provides multiple methods
to prove possession of the private key associated with
an identity.

    - TLS x509 certificates
    - Signature verification
    - Key Challenge

Authorization and access control is managed through a
distributed trust graph. Trust servers are used as the
authorities of the trust graph and allow caching portions
of the graph for faster access.

%package devel
BuildRequires:  golang >= 1.2.1-3
Requires:       golang >= 1.2.1-3
Summary:        Library for managing authentication and authorization
Provides:       golang(%{import_path}) = %{version}-%{release}
Provides:       golang(%{import_path}/trustgraph) = %{version}-%{release}
Provides:       golang(%{import_path}/testutil) = %{version}-%{release}

%description devel
%{summary}.

Authentication is handled using the identity attached
to the public key. Libtrust provides multiple methods
to prove possession of the private key associated with
an identity.

    - TLS x509 certificates
    - Signature verification
    - Key Challenge

Authorization and access control is managed through a
distributed trust graph. Trust servers are used as the
authorities of the trust graph and allow caching portions
of the graph for faster access.


%prep
%setup -qn %{repo}-%{commit}

%build

%install
install -dp %{buildroot}%{go_dir}/src/%{import_path}/trustgraph
cp -rpav {*.go,trustgraph,testutil} %{buildroot}%{go_dir}/src/%{import_path}/

%files devel
%doc CONTRIBUTING.md LICENSE MAINTAINERS README.md
%dir %{go_dir}/src/%{provider}.%{provider_tld}/%{project}
%dir %{go_dir}/src/%{import_path}
%{go_dir}/src/%{import_path}/*.go
%dir %{go_dir}/src/%{import_path}/trustgraph
%{go_dir}/src/%{import_path}/trustgraph/*.go
%dir %{go_dir}/src/%{import_path}/testutil
%{go_dir}/src/%{import_path}/testutil/*.go
