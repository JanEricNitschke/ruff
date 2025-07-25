import subprocess
from collections import deque
from collections.abc import Callable, Sequence
from typing import IO, Any
from typing_extensions import TypeAlias

from . import events, futures, protocols, transports

_File: TypeAlias = int | IO[Any] | None

class BaseSubprocessTransport(transports.SubprocessTransport):
    _closed: bool  # undocumented
    _protocol: protocols.SubprocessProtocol  # undocumented
    _loop: events.AbstractEventLoop  # undocumented
    _proc: subprocess.Popen[Any] | None  # undocumented
    _pid: int | None  # undocumented
    _returncode: int | None  # undocumented
    _exit_waiters: list[futures.Future[Any]]  # undocumented
    _pending_calls: deque[tuple[Callable[..., Any], tuple[Any, ...]]]  # undocumented
    _pipes: dict[int, _File]  # undocumented
    _finished: bool  # undocumented
    def __init__(
        self,
        loop: events.AbstractEventLoop,
        protocol: protocols.SubprocessProtocol,
        args: str | bytes | Sequence[str | bytes],
        shell: bool,
        stdin: _File,
        stdout: _File,
        stderr: _File,
        bufsize: int,
        waiter: futures.Future[Any] | None = None,
        extra: Any | None = None,
        **kwargs: Any,
    ) -> None: ...
    def _start(
        self,
        args: str | bytes | Sequence[str | bytes],
        shell: bool,
        stdin: _File,
        stdout: _File,
        stderr: _File,
        bufsize: int,
        **kwargs: Any,
    ) -> None: ...  # undocumented
    def get_pid(self) -> int | None: ...  # type: ignore[override]
    def get_pipe_transport(self, fd: int) -> _File: ...  # type: ignore[override]
    def _check_proc(self) -> None: ...  # undocumented
    def send_signal(self, signal: int) -> None: ...
    async def _connect_pipes(self, waiter: futures.Future[Any] | None) -> None: ...  # undocumented
    def _call(self, cb: Callable[..., object], *data: Any) -> None: ...  # undocumented
    def _pipe_connection_lost(self, fd: int, exc: BaseException | None) -> None: ...  # undocumented
    def _pipe_data_received(self, fd: int, data: bytes) -> None: ...  # undocumented
    def _process_exited(self, returncode: int) -> None: ...  # undocumented
    async def _wait(self) -> int:  # undocumented
        """Wait until the process exit and return the process return code.

        This method is a coroutine.
        """

    def _try_finish(self) -> None: ...  # undocumented
    def _call_connection_lost(self, exc: BaseException | None) -> None: ...  # undocumented
    def __del__(self) -> None: ...

class WriteSubprocessPipeProto(protocols.BaseProtocol):  # undocumented
    def __init__(self, proc: BaseSubprocessTransport, fd: int) -> None: ...

class ReadSubprocessPipeProto(WriteSubprocessPipeProto, protocols.Protocol): ...  # undocumented
