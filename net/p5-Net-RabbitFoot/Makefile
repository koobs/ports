PORTNAME=	Net-RabbitFoot
PORTVERSION=	1.03
PORTREVISION=	2
CATEGORIES=	net devel perl5
MASTER_SITES=	CPAN
MASTER_SITE_SUBDIR=	CPAN:IKUTA
PKGNAMEPREFIX=	p5-

MAINTAINER=	perl@FreeBSD.org
COMMENT=	Synchronous interface to AnyEvent::RabbitMQ
WWW=		https://metacpan.org/release/Net-RabbitFoot

LICENSE=	ART10 GPLv1+
LICENSE_COMB=	dual

BUILD_DEPENDS=	${RUN_DEPENDS}
RUN_DEPENDS=	p5-AnyEvent-RabbitMQ>=0:net/p5-AnyEvent-RabbitMQ \
		p5-Config-Any>=0:devel/p5-Config-Any \
		p5-Coro>=0:devel/p5-Coro \
		p5-JSON-XS>=0:converters/p5-JSON-XS \
		p5-List-MoreUtils>=0:lang/p5-List-MoreUtils \
		p5-Moose>=0:devel/p5-Moose \
		p5-MooseX-App-Cmd>=0:devel/p5-MooseX-App-Cmd \
		p5-MooseX-ConfigFromFile>=0:devel/p5-MooseX-ConfigFromFile
TEST_DEPENDS=	p5-Test-Exception>=0:devel/p5-Test-Exception

NO_ARCH=	yes

USES=		perl5
USE_PERL5=	configure

.include <bsd.port.mk>
