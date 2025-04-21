from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os
import argparse
from sklearn.metrics import jaccard_score, f1_score

    
    
def main():
    argParser = argparse.ArgumentParser()
    argParser.add_argument("--pred_pth")
    argParser.add_argument("--gt_pth")
    argParser.add_argument("--image_size", default=256)
    args = argParser.parse_args()
    pred_path = args.pred_pth
    gt_path = args.gt_pth
    image_size = args.image_size
    num = 0
    
    iou_list = []
    dice_list = []
    for root, dirs, files in os.walk(pred_path, topdown=False):
        for name in files:
            if 'ens' in name:
                num += 1
                ind = name.split('.')[0][:-11]
                print("current_image: ", ind)
                pred = Image.open(os.path.join(root, name)).convert('L')
                gt_name = ind + ".png"
                gt = Image.open(os.path.join(gt_path, gt_name)).convert('L').resize((image_size, image_size))
                
                gt = np.array(gt)
                pred = np.array(pred)
                pred = pred.astype(np.float32) / pred.max()
                th=0.5
                pred = (pred >= th).astype(np.uint8)
                
                pred_flat = pred.ravel()
                gt_flat = gt.ravel()

                iou = jaccard_score(gt_flat, pred_flat)      # IoU = TP / (TP + FP + FN)
                dice = f1_score(gt_flat, pred_flat)          # Dice = 2TP / (2TP + FP + FN)

                print(f"IoU  = {iou:.4f}")
                print(f"Dice = {dice:.4f}")
                
                iou_list.append(iou)
                dice_list.append(iou)

    print(f"Mean IoU = {np.mean(iou_list):.4f}")
    print(f"Mean Dice = {np.mean(dice_list):.4f}")
                
                
                
if __name__ == "__main__":
    main()