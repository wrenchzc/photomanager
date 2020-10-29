# photomanagger
a comand line photo manager 

我的照片已经多到感觉无法管理了, 终于决定写一个命令行工具来管理我的照片

初步设想实现以下功能
1. 查重, 使用md5查重. 
2. 命令行批量标签.
3. 命令行批量操作，如重命名，批量改大小等
4. 人脸识别.
5. 人脸聚类.
6. 自动打标签.

使用sqlite做数据库, 看看sqlite在几百万这个量级的性能如何

#### 命令行格式初定如下:
```
photo_manager command filter --option
```
#### command暂定以下几个
- **config** set or list the configuration
- **index** Index the photos in folder
- **display** display the images by condition
- **update** update address info by GPS info
- **tag** add tags to some photos
- **organize** organize photos, such as dedup, merge photo and so on

#### filter格式
```
field.condition:value
```
可以用空格分隔多个filter, 多个filter之间是and的关系, 若不符合上诉格式，则执行模糊搜索
##### field支持以下输入：
- date      日期
- person    人物
- tag       标签
- size      尺寸
- brand     相机品牌
- model     相机型号
- city      城市
##### condition支持以下输入:
- eq 等于
- gte 大于等于
- gt  大于
- lt  小于
- lte 小于等于
- sw  以xxx开始

#### 更新记录
- 2020-10-29:
  - 索引的时候加入gps信息
  - 新增指令根据GPS信息更新address
  - 模糊搜索的时候加入address字段
  