# HERE JUST FOR BACKWARD COMPATIBILITY
from backlash.tracing.errors import TraceErrorsMiddleware
from backlash.tracing.reporters.mail import EmailReporter
from backlash.tracing.reporters import sentry

import warnings
warnings.warn(
    'backlash.trace_errors is deprecated. Please use backlash.tracing.errors instead',
    DeprecationWarning)