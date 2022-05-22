# Generated by rust2rpm 21
%bcond_without check

%global crate names

Name:           rust-%{crate}
Version:        0.13.0
Release:        %autorelease
Summary:        Random name generator with names suitable for use in container instances, project names, application instances, etc

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/names
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
Random name generator with names suitable for use in container instances,
project names, application instances, etc.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE.txt
%doc CHANGELOG.md CODE_OF_CONDUCT.md README.md
%{_bindir}/names

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE.txt
%doc %{crate_instdir}/CHANGELOG.md
%doc %{crate_instdir}/CODE_OF_CONDUCT.md
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+application-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+application-devel %{_description}

This package contains library source intended for building other packages which
use the "application" feature of the "%{crate}" crate.

%files       -n %{name}+application-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+clap-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+clap-devel %{_description}

This package contains library source intended for building other packages which
use the "clap" feature of the "%{crate}" crate.

%files       -n %{name}+clap-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
