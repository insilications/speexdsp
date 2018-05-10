#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : speexdsp
Version  : 1.2rc3
Release  : 6
URL      : https://ftp.osuosl.org/pub/xiph/releases/speex/speexdsp-1.2rc3.tar.gz
Source0  : https://ftp.osuosl.org/pub/xiph/releases/speex/speexdsp-1.2rc3.tar.gz
Summary  : An open-source, patent-free speech codec
Group    : Development/Tools
License  : BSD-3-Clause
Requires: speexdsp-lib
Requires: speexdsp-doc
BuildRequires : pkgconfig(fftw3f)

%description
Speex is a patent-free audio codec designed especially for voice (unlike 
Vorbis which targets general audio) signals and providing good narrowband 
and wideband quality. This project aims to be complementary to the Vorbis
codec.

%package dev
Summary: dev components for the speexdsp package.
Group: Development
Requires: speexdsp-lib
Provides: speexdsp-devel

%description dev
dev components for the speexdsp package.


%package doc
Summary: doc components for the speexdsp package.
Group: Documentation

%description doc
doc components for the speexdsp package.


%package lib
Summary: lib components for the speexdsp package.
Group: Libraries

%description lib
lib components for the speexdsp package.


%prep
%setup -q -n speexdsp-1.2rc3
pushd ..
cp -a speexdsp-1.2rc3 buildavx2
popd
pushd ..
cp -a speexdsp-1.2rc3 buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1514681225
%configure --disable-static
make  %{?_smp_mflags}

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=haswell"
export CXXFLAGS="$CXXFLAGS -m64 -march=haswell"
export LDFLAGS="$LDFLAGS -m64 -march=haswell"
%configure --disable-static    --libdir=/usr/lib64/haswell --bindir=/usr/bin/haswell
make  %{?_smp_mflags}
popd
pushd ../buildavx512/
export CFLAGS="$CFLAGS -m64 -march=skylake-avx512"
export CXXFLAGS="$CXXFLAGS -m64 -march=skylake-avx512"
export LDFLAGS="$LDFLAGS -m64 -march=skylake-avx512"
%configure --disable-static    --libdir=/usr/lib64/haswell/avx512_1 --bindir=/usr/bin/haswell/avx512_1
make  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1514681225
rm -rf %{buildroot}
pushd ../buildavx2/
%make_install
popd
pushd ../buildavx512/
%make_install
popd
%make_install

%files
%defattr(-,root,root,-)
/usr/lib64/haswell/avx512_1/pkgconfig/speexdsp.pc
/usr/lib64/haswell/pkgconfig/speexdsp.pc

%files dev
%defattr(-,root,root,-)
/usr/include/speex/speex_echo.h
/usr/include/speex/speex_jitter.h
/usr/include/speex/speex_preprocess.h
/usr/include/speex/speex_resampler.h
/usr/include/speex/speexdsp_config_types.h
/usr/include/speex/speexdsp_types.h
/usr/lib64/haswell/libspeexdsp.so
/usr/lib64/libspeexdsp.so
/usr/lib64/pkgconfig/speexdsp.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/speexdsp/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/haswell/avx512_1/libspeexdsp.so
/usr/lib64/haswell/avx512_1/libspeexdsp.so.1
/usr/lib64/haswell/avx512_1/libspeexdsp.so.1.5.0
/usr/lib64/haswell/libspeexdsp.so.1
/usr/lib64/haswell/libspeexdsp.so.1.5.0
/usr/lib64/libspeexdsp.so.1
/usr/lib64/libspeexdsp.so.1.5.0
