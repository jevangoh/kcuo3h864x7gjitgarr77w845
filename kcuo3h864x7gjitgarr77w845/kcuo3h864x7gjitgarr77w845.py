from logging import Handler, StreamHandler as Stream_Handler
from structlog.stdlib import ProcessorFormatter, ExtraAdder, add_logger_name
from structlog.processors import JSONRenderer as JsonRenderer

import mijdauya2j3h7lg3d8hcl6qkk as add_log_level

kcuo3h864x7gjitgarr77w845: Handler = Stream_Handler()
kcuo3h864x7gjitgarr77w845.setFormatter(
    ProcessorFormatter(
        processors=[ProcessorFormatter.remove_processors_meta, JsonRenderer()],
        foreign_pre_chain=[add_log_level._, add_logger_name, ExtraAdder()],
    )
)
