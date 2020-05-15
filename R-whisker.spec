#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-whisker
Version  : 0.4
Release  : 64
URL      : https://cran.r-project.org/src/contrib/whisker_0.4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/whisker_0.4.tar.gz
Summary  : {{mustache}} for R, Logicless Templating
Group    : Development/Tools
License  : GPL-3.0
BuildRequires : buildreq-R

%description
No detailed description available

%prep
%setup -q -c -n whisker
cd %{_builddir}/whisker

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589518276

%install
export SOURCE_DATE_EPOCH=1589518276
rm -rf %{buildroot}
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
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library whisker
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library whisker
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library whisker
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc whisker || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/whisker/DESCRIPTION
/usr/lib64/R/library/whisker/INDEX
/usr/lib64/R/library/whisker/Meta/Rd.rds
/usr/lib64/R/library/whisker/Meta/features.rds
/usr/lib64/R/library/whisker/Meta/hsearch.rds
/usr/lib64/R/library/whisker/Meta/links.rds
/usr/lib64/R/library/whisker/Meta/nsInfo.rds
/usr/lib64/R/library/whisker/Meta/package.rds
/usr/lib64/R/library/whisker/NAMESPACE
/usr/lib64/R/library/whisker/NEWS
/usr/lib64/R/library/whisker/R/whisker
/usr/lib64/R/library/whisker/R/whisker.rdb
/usr/lib64/R/library/whisker/R/whisker.rdx
/usr/lib64/R/library/whisker/help/AnIndex
/usr/lib64/R/library/whisker/help/aliases.rds
/usr/lib64/R/library/whisker/help/paths.rds
/usr/lib64/R/library/whisker/help/whisker.rdb
/usr/lib64/R/library/whisker/help/whisker.rdx
/usr/lib64/R/library/whisker/html/00Index.html
/usr/lib64/R/library/whisker/html/R.css
/usr/lib64/R/library/whisker/specs/comments.json
/usr/lib64/R/library/whisker/specs/comments.yml
/usr/lib64/R/library/whisker/specs/convert.R
/usr/lib64/R/library/whisker/specs/delimiters.json
/usr/lib64/R/library/whisker/specs/delimiters.yml
/usr/lib64/R/library/whisker/specs/interpolation.json
/usr/lib64/R/library/whisker/specs/interpolation.yml
/usr/lib64/R/library/whisker/specs/inverted.json
/usr/lib64/R/library/whisker/specs/inverted.yml
/usr/lib64/R/library/whisker/specs/lambdas.json
/usr/lib64/R/library/whisker/specs/lambdas.yml
/usr/lib64/R/library/whisker/specs/partials.json
/usr/lib64/R/library/whisker/specs/partials.yml
/usr/lib64/R/library/whisker/specs/sections.json
/usr/lib64/R/library/whisker/specs/sections.yml
/usr/lib64/R/library/whisker/tests/testComments.R
/usr/lib64/R/library/whisker/tests/testName.R
/usr/lib64/R/library/whisker/tests/testdelimiters.R
/usr/lib64/R/library/whisker/tests/testinterpolation.R
/usr/lib64/R/library/whisker/tests/testinverted.R
/usr/lib64/R/library/whisker/tests/testpartials.R
/usr/lib64/R/library/whisker/tests/testsections.R
