from .ltx_keyframer import LTXKeyframer
from .multi_image_loader import MultiImageLoader
from .ltx_sequencer import LTXSequencer, LTXSequencerMirror
from .speech_length_calculator import SpeechLengthCalculator

# Register the node classes
NODE_CLASS_MAPPINGS = {
    "LTXKeyframer": LTXKeyframer,
    "MultiImageLoader": MultiImageLoader,
    "LTXSequencer": LTXSequencer,
    "LTXSequencerMirror": LTXSequencerMirror,
    "SpeechLengthCalculator": SpeechLengthCalculator
}

# Provide clean display names for the ComfyUI interface
NODE_DISPLAY_NAME_MAPPINGS = {
    "LTXKeyframer": "LTX Keyframer",
    "MultiImageLoader": "Multi Image Loader",
    "LTXSequencer": "LTX Sequencer",
    "LTXSequencerMirror": "LTX Sequencer Mirror",
    "SpeechLengthCalculator": "Speech Length Calculator"
}

WEB_DIRECTORY = "./js"

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS', 'WEB_DIRECTORY']