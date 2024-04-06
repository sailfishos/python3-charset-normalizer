Name:           python3-charset-normalizer
Version:        3.3.2
Release:        1
Summary:        The Real First Universal Charset Detector
License:        MIT
URL:            https://github.com/ousret/charset_normalizer
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  pkgconfig(python3)

%description
A library that helps you read text from an unknown charset encoding.
Motivated by chardet, trying to resolve the issue by taking
a new approach. All IANA character set names for which the Python core
library provides codecs are supported.

%prep
%autosetup -n %{name}-%{version}/upstream
# Remove pytest-cov settings from setup.cfg
sed -i "/addopts = --cov/d" setup.cfg

%build
%{py3_build}

%install
%{py3_install}

%files
%license LICENSE
%doc README.md
%{_bindir}/normalizer
%{python3_sitelib}/charset_normalizer
%{python3_sitelib}/charset_normalizer-*.egg-info
