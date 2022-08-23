#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-volatile
Version  : 2.1.0
Release  : 13
URL      : https://files.pythonhosted.org/packages/0d/c6/8ab8520c95262ba253e7cc93ba4636bdeeb9ab2c0bdec5034b46e01b607d/volatile-2.1.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/0d/c6/8ab8520c95262ba253e7cc93ba4636bdeeb9ab2c0bdec5034b46e01b607d/volatile-2.1.0.tar.gz
Summary  : A small extension for the tempfile module.
Group    : Development/Tools
License  : MIT
Requires: pypi-volatile-python = %{version}-%{release}
Requires: pypi-volatile-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
========
        
        Temporary files and directories.
        
        Contains replacement for ``tempfile.NamedTemporaryFile`` that does not delete
        the file on ``close()``, but still unlinks it after the context manager ends,
        as well as a ``mkdtemp``-based temporary directory implementation.
        
        * Mostly reuses the stdlib implementations, supporting the same signatures.
        * Due to that, uses the OS's built-in temporary file facilities, no custom
          schemes.
        * Tested on Python 2.6+ and 3.3+
        
        
        Usage
        -----
        
        A typical use-case that is not possible with the regular

%package python
Summary: python components for the pypi-volatile package.
Group: Default
Requires: pypi-volatile-python3 = %{version}-%{release}

%description python
python components for the pypi-volatile package.


%package python3
Summary: python3 components for the pypi-volatile package.
Group: Default
Requires: python3-core
Provides: pypi(volatile)

%description python3
python3 components for the pypi-volatile package.


%prep
%setup -q -n volatile-2.1.0
cd %{_builddir}/volatile-2.1.0
pushd ..
cp -a volatile-2.1.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656363162
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
