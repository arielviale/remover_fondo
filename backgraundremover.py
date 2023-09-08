import os
from datetime import datetime
from rembg import remove

class backgraundRemover:
    def __init__(self, input_folder, output_folder):
        self.input_folder = input_folder
        self.output_folder = output_folder
    
    def process_images(self):
        today = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        proccessed_folder = os.path.join(self.output_folder, today)
        os.makedirs(proccessed_folder, exist_ok=True)
        
        for filename in os.listdir(self.input_folder):
            if filename.endswith(('png','jpg','jpeg')):
                input_path = os.path.join(self.input_folder, filename)
                output_path = os.path.join(proccessed_folder, filename)
                self._remove_backgraund(input_path, output_path)
                self._move_originals(input_path, proccessed_folder)
                
    def _remove_backgraund(self, input_p, output_p):
        with open(input_p , 'rb') as inp , open(output_p , 'wb') as outp:
            backgraund_output = remove(inp.read())
            outp.write(backgraund_output)            
    
    def _move_originals(self , input_p , dest_p):   
        originals_folder = os.path.join(dest_p, 'originals')
        os.makedirs(originals_folder, exist_ok=True)
        
        filename = os.path.basename(input_p)
        new_path = os.path.join(originals_folder, filename)
        os.rename(input_p, new_path)
        
""" if __name__ == '__main__':
    input_folder = 'input'
    output_folder = 'output'
    
    remover = backgraundRemover(input_folder, output_folder)
    remove.process_images() """
                    
if __name__ == '__main__':
    input_folder = 'input'
    output_folder = 'output'
    
    remover = backgraundRemover(input_folder, output_folder)
    remover.process_images()      