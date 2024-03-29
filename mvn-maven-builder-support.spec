#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-maven-builder-support
Version  : 3.3.9
Release  : 4
URL      : https://repo1.maven.org/maven2/org/apache/maven/maven-builder-support/3.3.9/maven-builder-support-3.3.9.jar
Source0  : https://repo1.maven.org/maven2/org/apache/maven/maven-builder-support/3.3.9/maven-builder-support-3.3.9.jar
Source1  : https://repo1.maven.org/maven2/org/apache/maven/maven-builder-support/3.3.9/maven-builder-support-3.3.9.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-maven-builder-support-data = %{version}-%{release}
Requires: mvn-maven-builder-support-license = %{version}-%{release}
BuildRequires : apache-maven
BuildRequires : buildreq-mvn

%description
No detailed description available

%package data
Summary: data components for the mvn-maven-builder-support package.
Group: Data

%description data
data components for the mvn-maven-builder-support package.


%package license
Summary: license components for the mvn-maven-builder-support package.
Group: Default

%description license
license components for the mvn-maven-builder-support package.


%prep
%setup -q -n META-INF

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-maven-builder-support
cp LICENSE %{buildroot}/usr/share/package-licenses/mvn-maven-builder-support/LICENSE
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-builder-support/3.3.9
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-builder-support/3.3.9/maven-builder-support-3.3.9.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-builder-support/3.3.9
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-builder-support/3.3.9/maven-builder-support-3.3.9.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/apache/maven/maven-builder-support/3.3.9/maven-builder-support-3.3.9.jar
/usr/share/java/.m2/repository/org/apache/maven/maven-builder-support/3.3.9/maven-builder-support-3.3.9.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-maven-builder-support/LICENSE
