#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
#
Name     : R-pscl
Version  : 1.5.5.1
Release  : 41
URL      : https://cran.r-project.org/src/contrib/pscl_1.5.5.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/pscl_1.5.5.1.tar.gz
Summary  : Political Science Computational Laboratory
Group    : Development/Tools
License  : GPL-2.0
Requires: R-pscl-lib = %{version}-%{release}
Requires: R-pscl-license = %{version}-%{release}
BuildRequires : R-car
BuildRequires : R-lmtest
BuildRequires : R-sandwich
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
roll call analysis; computing highest density regions; maximum
	     likelihood estimation of zero-inflated and hurdle models for count
	     data; goodness-of-fit measures for GLMs; data sets used
	     in writing	and teaching at the Political Science
	     Computational Laboratory; seats-votes curves.

%package lib
Summary: lib components for the R-pscl package.
Group: Libraries
Requires: R-pscl-license = %{version}-%{release}

%description lib
lib components for the R-pscl package.


%package license
Summary: license components for the R-pscl package.
Group: Default

%description license
license components for the R-pscl package.


%prep
%setup -q -n pscl
pushd ..
cp -a pscl buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1683732124

%install
export SOURCE_DATE_EPOCH=1683732124
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/R-pscl
cp %{_builddir}/pscl/inst/COPYRIGHTS %{buildroot}/usr/share/package-licenses/R-pscl/6e55da8473fbb75c4a512d22a0919b50d7ec84f5 || :
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/pscl/CITATION
/usr/lib64/R/library/pscl/COPYRIGHTS
/usr/lib64/R/library/pscl/DESCRIPTION
/usr/lib64/R/library/pscl/INDEX
/usr/lib64/R/library/pscl/Meta/Rd.rds
/usr/lib64/R/library/pscl/Meta/data.rds
/usr/lib64/R/library/pscl/Meta/features.rds
/usr/lib64/R/library/pscl/Meta/hsearch.rds
/usr/lib64/R/library/pscl/Meta/links.rds
/usr/lib64/R/library/pscl/Meta/nsInfo.rds
/usr/lib64/R/library/pscl/Meta/package.rds
/usr/lib64/R/library/pscl/Meta/vignette.rds
/usr/lib64/R/library/pscl/NAMESPACE
/usr/lib64/R/library/pscl/NEWS
/usr/lib64/R/library/pscl/R/pscl
/usr/lib64/R/library/pscl/R/pscl.rdb
/usr/lib64/R/library/pscl/R/pscl.rdx
/usr/lib64/R/library/pscl/R/sysdata.rdb
/usr/lib64/R/library/pscl/R/sysdata.rdx
/usr/lib64/R/library/pscl/data/Rdata.rdb
/usr/lib64/R/library/pscl/data/Rdata.rds
/usr/lib64/R/library/pscl/data/Rdata.rdx
/usr/lib64/R/library/pscl/doc/countreg.R
/usr/lib64/R/library/pscl/doc/countreg.Rnw
/usr/lib64/R/library/pscl/doc/countreg.pdf
/usr/lib64/R/library/pscl/doc/index.html
/usr/lib64/R/library/pscl/extdata/id1.rda
/usr/lib64/R/library/pscl/extdata/id2.rda
/usr/lib64/R/library/pscl/help/AnIndex
/usr/lib64/R/library/pscl/help/aliases.rds
/usr/lib64/R/library/pscl/help/paths.rds
/usr/lib64/R/library/pscl/help/pscl.rdb
/usr/lib64/R/library/pscl/help/pscl.rdx
/usr/lib64/R/library/pscl/html/00Index.html
/usr/lib64/R/library/pscl/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/pscl/libs/pscl.so
/usr/lib64/R/library/pscl/libs/pscl.so.avx2
/usr/lib64/R/library/pscl/libs/pscl.so.avx512

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/R-pscl/6e55da8473fbb75c4a512d22a0919b50d7ec84f5
