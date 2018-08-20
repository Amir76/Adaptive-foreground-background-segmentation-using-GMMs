from .data_loader import DataLoader
import os
from scipy.misc import imread


class LASIESTADataLoader(DataLoader):

    _base_path = None
    _frames = None
    _next_frame_idx = 0

    def __init__(self, path):

        self._base_path = path

        files = os.listdir(path)

        # Sort files according to frame id
        files.sort(key=lambda file: int(file[file.find('-')+1:file.find('.')]))

        self._frames = files

    def get_next_frame(self):

        if self._next_frame_idx < len(self._frames):
            path_to_frame = os.path.join(self._base_path, self._frames[self._next_frame_idx])
            frame = imread(path_to_frame)
            self._next_frame_idx += 1
            return frame

        return None
