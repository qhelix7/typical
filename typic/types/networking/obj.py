import dataclasses

from ..secret import SecretStr


@dataclasses.dataclass(frozen=True)
class NetAddrInfo:
    """Detailed information about a network address.

    Can be called directly, generated by casting a :py:class:`str` as
    :py:class:`NetworkAddress`, or created with :py:meth:`NetAddrInfo.from_str`
    """

    scheme: str
    """The net-address scheme, e.g., ``http``, ``tcp``, ``ssh``, etc."""
    auth: str
    """The user auth info."""
    password: SecretStr
    """The user's password."""
    host: str
    """The host for this addres, e.g. ``0.0.0.0``, ``foobar.net``."""
    port: int
    """The port for this net-address"""
    path: str
    """The URI path."""
    qs: str
    """The query-string, unparsed, e.g. ``?id=1&name=foo``"""
    params: str
    """The url parameters, unparsed, e.g. ``id=2;foo=bar``"""
    fragment: str
    """The uri fragment, e.g. ``#some-page-anchor``"""
    is_ip: bool = False


@dataclasses.dataclass(frozen=True)
class EmailAddrInfo:
    name: str
    """The proper name associated to the email."""
    username: str
    """The username portion of the email."""
    host: str
    """The host address where the email server is located."""
    is_ip: bool = False


@dataclasses.dataclass(frozen=True)
class DSNInfo:
    """Detailed information about a D(ata)S(ource)N(ame).

    Can be called directly, generated by casting a :py:class:`str` as :py:class:`DSN`,
    or created with :py:meth:`DSNInfo.from_str`

    Notes
    -----
    DSNs are *technically* a type of network address, but are more strict.
    There's also a semi-standard API for interacting with them, thanks to SQLAlchemy, etc.
    So we have our own ``-Info`` object which conforms more closely with the expected API.

    See Also
    --------
    :py:class:`typic.types.NetAddrInfo`
    """

    driver: str
    """The database driver, e.g., ``mysql``."""
    username: str
    """The username used for authentication."""
    password: SecretStr
    """The password used for authentication."""
    host: str
    """The host address where the server is located."""
    port: int
    """The exposed port to connect to."""
    name: str
    """The database name."""
    qs: str
    """The query-string to pass on to the database."""
    is_ip: bool = False