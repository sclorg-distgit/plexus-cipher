%{?scl:%scl_package plexus-cipher}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}plexus-cipher
Version:        1.7
Release:        12.2%{?dist}
Summary:        Plexus Cipher: encryption/decryption Component
License:        ASL 2.0
# project moved to GitHub and it looks like there is no official website anymore
URL:            https://github.com/codehaus-plexus/plexus-cipher
BuildArch:      noarch

# git clone https://github.com/sonatype/plexus-cipher.git
# cd plexus-cipher/
# note this is version 1.7 + our patches which were incorporated by upstream maintainer
# git archive --format tar --prefix=plexus-cipher-1.7/ 0cff29e6b2e | gzip -9 > plexus-cipher-1.7.tar.gz
Source0:        %{pkg_name}-%{version}.tar.gz

BuildRequires:  %{?scl_prefix}maven-local
BuildRequires:  %{?scl_prefix}mvn(javax.enterprise:cdi-api)
BuildRequires:  %{?scl_prefix}mvn(javax.inject:javax.inject)
BuildRequires:  %{?scl_prefix}mvn(junit:junit)
BuildRequires:  %{?scl_prefix}mvn(org.sonatype.plugins:sisu-maven-plugin)
BuildRequires:  %{?scl_prefix}mvn(org.sonatype.spice:spice-parent:pom:)

%description
Plexus Cipher: encryption/decryption Component

%package javadoc
Summary:        Javadoc for %{pkg_name}

%description javadoc
API documentation for %{pkg_name}.

%prep
%setup -n %{pkg_name}-%{version} -q

# replace %{version}-SNAPSHOT with %{version}
%pom_xpath_replace pom:project/pom:version "<version>%{version}</version>"

# fedora moved from sonatype sisu to eclipse sisu. sisu-inject-bean artifact
# doesn't exist in eclipse sisu. this artifact contains nothing but
# bundled classes from atinject, cdi-api, aopalliance and maybe others.
%pom_remove_dep org.sonatype.sisu:sisu-inject-bean
%pom_add_dep javax.inject:javax.inject:1:provided
%pom_add_dep javax.enterprise:cdi-api:1.0:provided

%mvn_file : plexus/%{pkg_name}

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Thu Jun 22 2017 Michael Simacek <msimacek@redhat.com> - 1.7-12.2
- Mass rebuild 2017-06-22

* Wed Jun 21 2017 Java Maintainers <java-maint@redhat.com> - 1.7-12.1
- Automated package import and SCL-ization

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 14 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.7-9
- Cleanup package

* Wed Apr  1 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.7-8
- Update upstream URL

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.7-6
- Use Requires: java-headless rebuild (#1067528)

* Thu Nov 14 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.7-5
- Migrate from sisu-maven-plugin to sisu-mojos

* Mon Aug 05 2013 Michal Srb <msrb@redhat.com> - 1.7-4
- Fix FTBFS (Resolves: #992802)
- Adapt to current guidelines

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar 13 2013 Michal Srb <msrb@redhat.com> - 1.7-1
- Update to upstream version 1.7

* Thu Feb 21 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.5-15
- Reemove BR: plexus-container-default

* Fri Feb 08 2013 Michal Srb <msrb@redhat.com> - 1.5-14
- Remove unnecessary dependency on plexus-containers (#908586)

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.5-13
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Wed Jan 02 2013 Michal Srb <msrb@redhat.com> - 1.5-12
- Fixed URL (Resolves: #880322)

* Tue Nov 27 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.5-11
- Improve randomness of PBECipher
- Resolves: rhbz#880279

* Mon Nov 26 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.5-10
- Remove duplicated NOTICE file

* Mon Nov 26 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.5-9
- Add ASL 2.0 text and install NOTICE file

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 26 2011 Jaromir Capik <jcapik@redhat.com> - 1.5-6
- Migration from plexus-maven-plugin to plexus-containers-component-metadata
- Minor spec file changes according to the latest guidelines

* Fri Jun 3 2011 Alexander Kurtakov <akurtako@redhat.com> 1.5-5
- Do not require maven2.
- Build with maven (v. 3) by default.
- drop obsoleted parts of the spec.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jun 01 2010 Hui Wang <huwang@redhat.com> - 1.5-3
- Add NOTICE.text
- Fix URL
- Fix direction of install pom

* Sun May 23 2010 Hui Wang <huwang@redhat.com> - 1.5-2
- Correct URL

* Tue May 18 2010 Hui Wang <huwang@redhat.com> - 1.5-1
- Initial version of the package
