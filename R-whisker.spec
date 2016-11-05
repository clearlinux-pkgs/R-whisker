#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-whisker
Version  : 0.3
Release  : 25
URL      : http://cran.r-project.org/src/contrib/whisker_0.3-2.tar.gz
Source0  : http://cran.r-project.org/src/contrib/whisker_0.3-2.tar.gz
Summary  : {{mustache}} for R, logicless templating
Group    : Development/Tools
License  : GPL-3.0
BuildRequires : clr-R-helpers

%description
No detailed description available

%prep
%setup -q -c -n whisker

%build

%install
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --build  -l %{buildroot}/usr/lib64/R/library whisker
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library whisker


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/whisker/DESCRIPTION
/usr/lib64/R/library/whisker/INDEX
/usr/lib64/R/library/whisker/Meta/Rd.rds
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
/usr/lib64/R/library/whisker/tests/testdelimiters.R
/usr/lib64/R/library/whisker/tests/testinterpolation.R
/usr/lib64/R/library/whisker/tests/testinverted.R
/usr/lib64/R/library/whisker/tests/testpartials.R
/usr/lib64/R/library/whisker/tests/testsections.R
