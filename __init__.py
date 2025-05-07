from .inpaint_cropandstitch import InpaintCropImproved
from .inpaint_cropandstitch import InpaintStitchImproved

# OLD
from .inpaint_cropandstitch_old import InpaintCrop
from .inpaint_cropandstitch_old import InpaintStitch
from .inpaint_cropandstitch_old import InpaintExtendOutpaint
from .inpaint_cropandstitch_old import InpaintResize

WEB_DIRECTORY = "js"

NODE_CLASS_MAPPINGS = {
    "InpaintCropImproved": InpaintCropImproved,
    "InpaintStitchImproved": InpaintStitchImproved,

    # OLD
    "InpaintCrop": InpaintCrop,
    "InpaintStitch": InpaintStitch,
    "InpaintExtendOutpaint": InpaintExtendOutpaint,
    "InpaintResize": InpaintResize,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "InpaintCropImproved": "Custom_LOGIC_improved_crop_inpaint",
    "InpaintStitchImproved": "Custom_LOGIC_improved_stitch_inpaint",

    # OLD
    "InpaintCrop": "(OLD 💀, use the new ✂️ Inpaint Crop node)",
    "InpaintStitch": "(OLD 💀, use the new ✂️ Inpaint Stitch node)",
    "InpaintExtendOutpaint": "(OLD 💀 use Crop instead) Extend Image for Outpainting",
    "InpaintResize": "(OLD 💀 use Crop instead) Resize Image Before Inpainting",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
