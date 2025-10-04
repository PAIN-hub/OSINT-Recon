import os
import hashlib
from PIL import Image
import exifread

def hash_file(path, algo="sha256", chunk_size=8192):
    h = hashlib.new(algo)
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(chunk_size), b""):
            h.update(chunk)
    return h.hexdigest()

def extract_metadata(path):
    """Extract file info, hashes, and image EXIF metadata."""
    data = {"type": "file", "path": path}
    if not os.path.exists(path):
        data["error"] = "File not found"
        return data

    data["size_bytes"] = os.path.getsize(path)
    data["hashes"] = {
        "md5": hash_file(path, "md5"),
        "sha1": hash_file(path, "sha1"),
        "sha256": hash_file(path, "sha256"),
    }

    if path.lower().endswith((".jpg", ".jpeg", ".png")):
        try:
            with open(path, "rb") as f:
                tags = exifread.process_file(f)
                data["exif"] = {tag: str(val) for tag, val in tags.items()}
        except Exception as e:
            data["exif_error"] = str(e)

    return data