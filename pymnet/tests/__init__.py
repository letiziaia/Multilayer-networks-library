from net_test import test_net
from cc_test import test_cc
from diagnostics_test import test_diagnostics
from io_test import test_io
from models_test import test_models
from transforms_test import test_transforms
from visuals_test import test_visuals

def test_all():
    test_net()
    test_cc()
    test_diagnostics()
    test_io()
    test_models()
    test_transforms()
    test_visuals()
