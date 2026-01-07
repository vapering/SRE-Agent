# ⚡ Flash Sale Mall - 秒杀商城系统

一个专为SRE团队设计的手机秒杀商城系统，用于测试故障检测、根因分析和系统恢复能力。

## 🎯 项目概述

Flash Sale Mall 是一个高度简化的手机秒杀商城系统，支持高并发场景下的故障注入和监控分析。系统提供完整的用户认证、商品秒杀、订单管理和监控功能。

## 🏗️ 技术架构

### 前端技术栈
- **React 18** + **TypeScript** - 现代化前端框架
- **Vite** - 快速构建工具
- **TailwindCSS** - 实用优先的CSS框架
- **React Router** - 客户端路由管理
- **Zustand** - 轻量级状态管理
- **Lucide React** - 图标库

### 后端技术栈（已迁移为Spring Boot）
- **Spring Boot 3.3.x** + **Java 21** - 企业级后端框架
- **Spring Security + JWT** - 认证授权
- **Spring Data JPA/Hibernate** - ORM与数据访问
- **MySQL 8.0** - 关系型数据库
- **Redis 7.0** - 缓存与限流
- **Apache Kafka** - 异步消息处理
- **Micrometer + Prometheus** - 指标采集
- **SkyWalking Java Agent** - 链路追踪

### 监控和运维
- **Prometheus** - 指标收集
- **Grafana** - 可视化监控面板
- **Docker** - 容器化部署

## 🚀 快速开始

### 环境要求
- Docker 与 Docker Compose（后端容器化）
- Node.js 18+（本地前端开发可选）

### 1. 启动基础设施与监控
```bash
# 启动数据库、缓存、消息队列与监控
docker compose up -d mysql redis zookeeper kafka prometheus grafana loki promtail oap skywalking-ui
```

### 2. 安装依赖
```bash
npm install
```

### 3. 启动后端服务（Spring Boot容器）
```bash
docker compose up -d backend
docker compose logs -f backend
```

### 4. 启动前端服务
```bash
# 开发模式
npm run dev

# 构建生产版本
npm run build
```

### 5. 访问应用
- 前端应用: http://localhost:5173
- 后端API: http://localhost:3001
- Grafana监控: http://localhost:3000 (admin/admin123)
- Prometheus: http://localhost:9090
- SkyWalking UI: http://localhost:8080

## 📋 核心功能

### 用户系统
- ✅ 用户登录/认证 (JWT)
- ✅ 会话管理
- ✅ 权限控制

### 商品秒杀
- ✅ 商品展示和搜索
- ✅ 实时倒计时
- ✅ 秒杀状态管理
- ✅ 库存管理
- ✅ 频率限制 (10秒3次)

### 订单管理
- ✅ 订单创建
- ✅ 订单状态跟踪
- ✅ 订单历史查询

### 监控
- ✅ 实时性能指标（Micrometer/Prometheus）
- ✅ QPS、响应时间、错误率监控
- ✅ 并发用户数统计
- ✅ 系统健康检查
- ✅ 链路追踪（SkyWalking）

## 🔧 API接口

### 认证接口
- `POST /api/auth/login` - 用户登录
- `POST /api/auth/logout` - 用户登出
- `GET /api/auth/me` - 获取当前用户信息

### 商品接口
- `GET /api/products` - 获取商品列表
- `GET /api/products/:id` - 获取商品详情

### 秒杀接口
- `POST /api/seckill` - 提交秒杀请求 (需要认证)

### 订单接口
- `GET /api/orders` - 获取用户订单 (需要认证)
- `GET /api/orders/:id` - 获取订单详情 (需要认证)

## 🎨 用户界面

### 设计原则
- **移动端优先** - 响应式设计
- **红色主题** - 突出秒杀氛围 (#E53E3E)
- **卡片式布局** - 清晰的信息层次
- **实时交互** - 流畅的用户体验

### 页面结构
1. **登录页面** - 简洁的认证界面
2. **秒杀首页** - 商品网格和倒计时
3. **订单页面** - 订单管理和状态跟踪
4. **监控面板** - 实时指标

## 🧪 测试账户

```
普通用户:
- 用户名: testuser
- 密码: test123

管理员:
- 用户名: admin  
- 密码: admin123
```

## 📊 监控指标

### 性能指标
- **QPS (Queries Per Second)** - 每秒查询数
- **响应时间** - API响应延迟
- **错误率** - 请求失败百分比
- **并发用户数** - 同时在线用户数量

### 系统状态
- **数据库连接** - MySQL健康状态
- **Redis缓存** - 缓存服务状态
- **消息队列** - Kafka服务状态

## 🔍 故障注入测试

支持多种故障类型模拟：
- **数据库连接池耗尽** - 测试数据库压力
- **Kafka消息积压** - 测试消息队列处理能力
- **缓存击穿** - 测试缓存失效场景
- **API限流** - 测试限流机制
- **服务超时** - 测试超时处理

## 🛠️ 开发指南

### 项目结构
```
FlashSaleMall/
├── src/                    # 前端源代码
│   ├── components/         # React组件
│   ├── pages/             # 页面组件
│   ├── stores/            # Zustand状态管理
│   └── ...
├── backend-spring/        # Spring Boot后端
│   ├── src/main/java/     # 业务代码（Controller/Repository/Config）
│   ├── src/main/resources # 配置（application.yml）
│   ├── src/test/java/     # 测试用例
│   └── Dockerfile         # 生产容器镜像（含SkyWalking Agent）
├── docker-compose.yml    # Docker服务配置
└── ...
```

### 常用开发与运维命令
```bash
# 前端开发
npm install && npm run dev

# 后端容器
docker compose up -d backend
docker compose logs -f backend

# 基础设施与监控
docker compose up -d mysql redis zookeeper kafka prometheus grafana loki promtail oap skywalking-ui

# 关闭服务
docker compose down
```

## 🔒 安全特性

- **JWT认证** - Spring Security + JWT
- **密码加密** - BCryptPasswordEncoder
- **频率限制** - Redis计数器实现（10秒3次）
- **输入验证** - 控制器层参数校验
- **错误处理** - Spring 全局异常处理（统一响应格式）

## 📈 性能优化

- **Redis缓存** - 商品信息和库存缓存
- **数据库连接池** - HikariCP 连接池
- **异步处理** - Kafka异步消息
- **前端优化** - 代码分割和懒加载
