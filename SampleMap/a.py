import os
import csv
import json
import shutil
from PIL import Image

# 定义根目录
root_dir = './objects'

name = []

# 遍历根目录下的所有子文件夹
for idx, subdir in enumerate(os.listdir(root_dir)):
    
    name.append(subdir)
    

open('name.txt', 'w').write('\n'.join(name))
    
    # subdir_path = os.path.join(root_dir, subdir)
    # if os.path.isdir(subdir_path):  # 确保是文件夹
    #     maze_path = os.path.join(subdir_path, 'maze')
    #     special_blocks_path = os.path.join(subdir_path, 'special_blocks')
    #     maze_meta_info_path = os.path.join(subdir_path, 'maze_meta_info.json')
    #     wrong_maze_path = os.path.join(maze_path, 'special_blocks')
    #     wrong_meta_path = os.path.join(maze_path, 'maze_meta_info.json')
    #     game_object_blocks_path = os.path.join(special_blocks_path, 'game_object_blocks.csv')

        # if os.path.exists(wrong_maze_path):
        #     shutil.rmtree(wrong_maze_path)
        # if os.path.exists(wrong_meta_path):
        #     os.remove(wrong_meta_path)
        
        # # 如果 maze 文件夹不存在，则创建
        
        # if not os.path.exists(maze_path):
        #     os.makedirs(maze_path)
        
        # # 如果 special_blocks 文件夹不存在，则创建
        # if not os.path.exists(special_blocks_path):
        #     os.makedirs(special_blocks_path)
        
        # # 如果 maze_meta_info.json 文件不存在，则创建
        
        # texture_path = os.path.join(subdir_path, 'texture.png')
        # if os.path.exists(texture_path):
        #     with Image.open(texture_path) as img:
        #         width, height = img.size
        #         if width % 32 == 0:
        #             maze_width = max(1, int(width // 32))
        #             maze_height = max(1, int(height // 32))
        #         else:
        #             maze_width = max(1, int(width // 100))
        #             maze_height = max(1, int(height // 100))
        #             print("1",subdir_path, maze_height, maze_width)
        #             with open(maze_meta_info_path, 'w') as f:
                
        #                 json.dump({
        #                 "typeId": idx+10,
        #                 "world_name": subdir,
        #                 "maze_width": maze_width,
        #                 "maze_height": maze_height,
        #                 "sq_tile_size": 32.0,
        #                 "special_constraint": ""
        #                 }, f)
        # else:
        #     maze_width = 1
        #     maze_height = 1
        
        # # 如果 maze 文件夹是空的，就新建两个 csv 文件
        # if not os.listdir(maze_path):  # 检查 maze 文件夹是否为空
        #     if os.path.exists(maze_meta_info_path):
        #         with open(maze_meta_info_path, 'r') as f:
        #             meta_info = json.load(f)
        #             maze_width = meta_info.get('maze_width', 1)
        #             maze_height = meta_info.get('maze_height', 1)
            
        #     # 创建 collision_maze.csv 文件，全 0
        #     collision_maze_path = os.path.join(maze_path, 'collision_maze.csv')
        #     with open(collision_maze_path, 'w', newline='') as f:
        #         writer = csv.writer(f)
        #         for _ in range(maze_height):
        #             writer.writerow([0] * maze_width)
            
        #     # 创建 game_object_maze.csv 文件，全 1
        #     game_object_maze_path = os.path.join(maze_path, 'game_object_maze.csv')
        #     with open(game_object_maze_path, 'w', newline='') as f:
        #         writer = csv.writer(f)
        #         for _ in range(maze_height):
        #             writer.writerow([1] * maze_width)
        
        # 如果 game_object_blocks.csv 文件不存在，则创建
        # with open(game_object_blocks_path, 'w') as f:
        #     f.write(f'1,{subdir}')