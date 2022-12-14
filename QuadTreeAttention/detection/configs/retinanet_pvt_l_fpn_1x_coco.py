_base_ = [
    '_base_/models/retinanet_r50_fpn.py',
    '_base_/datasets/coco_detection.py',
    '_base_/schedules/schedule_1x.py',
    '_base_/default_runtime.py'
]
model = dict(
    # pretrained='pretrained/pvt_large.pth',
    pretrained='https://github.com/whai362/PVT/releases/download/v2/pvt_large.pth',
    backbone=dict(
        type='pvt_large',
        style='pytorch'),
    neck=dict(
        type='FPN',
        in_channels=[64, 128, 320, 512],
        out_channels=256,
        start_level=1,
        add_extra_convs='on_input',
        num_outs=5))

optimizer = dict(_delete_=True, type='AdamW', lr=0.0001, weight_decay=0.0001)

#fp16
runner = dict(type='EpochBasedRunnerAmp', max_epochs=12)
fp16 = None
optimizer_config = dict(
    type="DistOptimizerHook",
    update_interval=1,
    grad_clip=None,
    coalesce=True,
    bucket_size_mb=-1,
    use_fp16=True,
)

find_unused_parameters = True
