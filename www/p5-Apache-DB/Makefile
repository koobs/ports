PORTNAME=	Apache-DB
PORTVERSION=	0.18
PORTREVISION=	1
CATEGORIES=	www perl5
MASTER_SITES=	CPAN
PKGNAMEPREFIX=	p5-

MAINTAINER=	perl@FreeBSD.org
COMMENT=	Debugging and profiling tools for mod_perl
WWW=		https://metacpan.org/release/Apache-DB

LICENSE=	ART10 GPLv1+
LICENSE_COMB=	dual

RUN_DEPENDS=	${APACHE_PKGNAMEPREFIX}mod_perl2>=0:www/mod_perl2

USES=		apache:run perl5
USE_PERL5=	configure

post-install:
	${STRIP_CMD} ${STAGEDIR}${PREFIX}/${SITE_ARCH_REL}/auto/Apache/DB/DB.so

.include <bsd.port.pre.mk>

.if ${PERL_LEVEL} >= 503700
BROKEN=         uses hidden Perl functions that are hidden after 5.37.0
.endif

.include <bsd.port.post.mk>
