# arXiv 自动驾驶论文

Generated: 2026-05-12 08:01 UTC

当前展示 20 篇论文的最新版本。旧版本只保留 arXiv 链接。

<table style="table-layout: fixed; width: 100%;">
  <colgroup>
    <col style="width: 23%;">
    <col style="width: 13%;">
    <col style="width: 10%;">
    <col style="width: 34%;">
    <col style="width: 20%;">
  </colgroup>
  <thead>
    <tr>
      <th>标题 / 作者</th>
      <th>信息</th>
      <th>关键词</th>
      <th>摘要</th>
      <th>简短总结</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>1. See Tomorrow, Act Today: Foresight-Driven Autonomous Driving</strong><br><span>Bozhou Zhang, Nan Song, Yuang Wang, Jiankang Deng, Xiatian Zhu, Li Zhang</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-05-08</div><div>2026-05-08</div><div><a href="http://arxiv.org/abs/2605.07195v1">2605.07195v1</a> / <a href="https://arxiv.org/pdf/2605.07195v1">PDF</a></div><div>cs.CV</div></td>
      <td style="width: 10%; vertical-align: top;">world model</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>当前的端到端自动驾驶规划器本质上是被动的：它们根据历史和当前的观测来预测未来的动作。我们认为，自动驾驶智能体应该在做出决定之前想象未来的场景，就像人类驾驶员在行动前会心理模拟“接下来会发生什么”一样。我们引入了 ForeSight，一个以基础世界模型为中心的规划框架，它将自动驾驶重新定义为预见性决策。ForeSight 没有将世界模型视为辅助组件，而是将未来场景的想象作为动作预测的主要驱动力。我们的方法分两个阶段运行：（1）通过预训练的世界模型生成合理的未来视觉世界，以及（2）根据这些想象的未来规划动作。这种从“我现在该做什么？”到“会发生什么，我该如何应对？”的范式转变，实现了真正的预见性规划而非被动式规划。通过将决策基于预期的情境而非仅仅当前的观测，ForeSight 更有效地应对动态、交互式场景。在 NAVSIM 和 nuScenes 上的大量实验表明，显式的未来想象显著优于之前的最先进替代方案，验证了我们这种预见性驱动的方法。</td>
      <td style="width: 20%; vertical-align: top;">当前自动驾驶规划器多为被动式，仅依据历史和当前观测做决策。本论文提出了 ForeSight 框架，通过引入基础世界模型来想象未来场景，进而在此基础上规划动作，将自动驾驶重塑为预见性决策。实验结果表明，这种预见性驱动的方法能够更有效地应对动态交互场景，并显著超越了现有最先进的替代方案。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>2. GSDrive: Reinforcing Driving Policies by Multi-mode Trajectory Probing with 3D Gaussian Splatting Environment</strong><br><span>Ziang Guo, Chen Min, Xuefeng Zhang, Yixiao Zhou, Zufeng Zhang, Dzmitry Tsetserukou</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-04-30</div><div>2026-05-01</div><div><a href="http://arxiv.org/abs/2604.28111v2">2604.28111v2</a> / <a href="https://arxiv.org/pdf/2604.28111v2">PDF</a></div><div>cs.RO</div></td>
      <td style="width: 10%; vertical-align: top;">RL</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>端到端（E2E）自动驾驶提供了一种有前景的方法，可将感知输入直接转化为驾驶动作。然而，高昂的标注成本和时序数据质量下降阻碍了其长期实际部署。尽管结合模仿学习（IL）和强化学习（RL）是改进策略的常见策略，但传统的RL训练依赖于延迟的、基于事件的奖励——策略仅从碰撞等灾难性结果中学习，导致过早收敛到次优行为。为了解决这些局限性，我们引入了GSDrive，这是一个利用3D高斯泼溅（3DGS）进行端到端驾驶策略改进中可微分、基于物理的奖励塑形的框架。我们的方法在3DGS模拟器中整合了一个基于流匹配的轨迹预测器，实现了多模态轨迹探测，其中候选轨迹被模拟以评估预期奖励。这通过将奖励函数建立在物理模拟的交互信号上，在IL和RL之间建立了双向知识交换，提供了即时密集反馈，而非稀疏的灾难性事件。在重建的nuScenes数据集上进行评估，我们的方法在闭环实验中超越了现有基于仿真的RL驾驶方法。代码可在 https://github.com/ZionGo6/GSDrive 获取。</td>
      <td style="width: 20%; vertical-align: top;">端到端自动驾驶面临高昂标注成本和传统强化学习中稀疏、延迟奖励导致策略次优的问题。GSDrive提出了一个框架，利用3D高斯泼溅（3DGS）在端到端驾驶策略改进中提供可微分、基于物理的奖励塑形，并通过在3DGS模拟器中嵌入流匹配的轨迹预测器进行多模态轨迹探测来评估潜在奖励。该方法在模仿学习和强化学习之间建立了双向知识交换，提供即时密集反馈，并在重建的nuScenes数据集上的闭环实验中超越了现有基于仿真的RL驾驶方法。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>3. ProDrive: Proactive Planning for Autonomous Driving via Ego-Environment Co-Evolution</strong><br><span>Chuyao Fu, Shengzhe Gan, Zhuoli Ouyang, Yuhan Rui, Xiaowei Chi, Sirui Han, Jiankun Wang, Hong Zhang</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-04-28</div><div>2026-04-28</div><div><a href="http://arxiv.org/abs/2604.25329v1">2604.25329v1</a> / <a href="https://arxiv.org/pdf/2604.25329v1">PDF</a></div><div>cs.RO</div></td>
      <td style="width: 10%; vertical-align: top;">world model</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>端到端自动驾驶规划器通常仅根据当前观测生成轨迹。然而，现实世界的驾驶高度动态，这种反应式规划无法预测未来的场景演变，常常导致短视决策和安全关键故障。我们提出了 ProDrive，一个基于世界模型的主动规划框架，它能够实现自动驾驶中的自我-环境协同演化。ProDrive 端到端地联合训练一个以查询为中心的轨迹规划器和一个鸟瞰图（BEV）世界模型：规划器生成多样化的候选轨迹和规划感知的自我令牌，而世界模型则根据这些信息预测未来的场景演变。通过将规划器特征注入世界模型并并行评估所有候选方案，ProDrive 保留了端到端梯度流，并允许对未来结果的评估直接影响规划。这种双向耦合使得主动规划超越了当前观测驱动的决策。在 NAVSIM v1 上的实验表明，ProDrive 在安全性和规划效率方面均优于强大的基线，而消融实验则验证了所提出的自我-环境耦合设计的有效性。</td>
      <td style="width: 20%; vertical-align: top;">传统自动驾驶规划器仅依赖当前观测，导致在动态环境中做出短视且可能不安全的决策。ProDrive 提出一个基于世界模型的主动规划框架，通过端到端地联合训练轨迹规划器和世界模型，实现自我-环境协同演化。该方法通过将规划器特征注入世界模型并评估未来结果来指导规划，实验证明其在安全性和规划效率上优于现有基线。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>4. Reasoning About Traversability: Language-Guided Off-Road 3D Trajectory Planning</strong><br><span>Byounggun Park, Soonmin Hwang</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-04-23</div><div>2026-04-23</div><div><a href="http://arxiv.org/abs/2604.21249v1">2604.21249v1</a> / <a href="https://arxiv.org/pdf/2604.21249v1">PDF</a></div><div>cs.RO</div></td>
      <td style="width: 10%; vertical-align: top;">VLM</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>尽管视觉-语言模型（VLM）能够为端到端自动驾驶（尤其是在非结构化环境中）提供高级语义推理能力，但现有的越野数据集存在语言标注与车辆动作和地形几何形状弱对齐的问题。为解决这种不对齐问题，我们提出了一种语言精炼框架，将标注重构为与动作对齐的对，使VLM能够直接从单张图像生成精炼的场景描述和3D未来轨迹。为了进一步鼓励地形感知规划，我们引入了一种偏好优化策略，该策略构建了几何感知硬负样本，并明确惩罚与局部高程剖面不一致的轨迹。此外，我们提出了越野专用指标来量化可通行性符合度和高程一致性，解决了传统公路评估的局限性。在ORAD-3D基准上的实验表明，我们的方法将平均轨迹误差从1.01米降低到0.97米，将可通行性符合度从0.621提高到0.644，并将高程不一致性从0.428降低到0.322，这突出了动作对齐监督和地形感知优化对于鲁棒越野驾驶的有效性。</td>
      <td style="width: 20%; vertical-align: top;">针对越野自动驾驶中语言标注与车辆动作和地形几何结构不匹配的问题，本文提出了一种语言精炼框架，将标注重构为与动作对齐的对，并引入偏好优化策略，通过几何感知硬负样本来鼓励地形感知规划。该方法使视觉-语言模型能够直接从图像生成地形感知的3D轨迹。在ORAD-3D基准上的实验表明，本文方法显著降低了轨迹误差，提高了可通行性符合度并减少了高程不一致性，验证了其在鲁棒越野驾驶中的有效性。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>5. SpanVLA: Efficient Action Bridging and Learning from Negative-Recovery Samples for Vision-Language-Action Model</strong><br><span>Zewei Zhou, Ruining Yang, Xuewei, Qi, Yiluan Guo, Sherry X. Chen, Tao Feng, Kateryna Pistunova, Yishan Shen, Lili Su, Jiaqi Ma</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-04-21</div><div>2026-04-21</div><div><a href="http://arxiv.org/abs/2604.19710v1">2604.19710v1</a> / <a href="https://arxiv.org/pdf/2604.19710v1">PDF</a></div><div>cs.CV</div></td>
      <td style="width: 10%; vertical-align: top;">VLM</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>视觉-语言-动作 (VLA) 模型提供了一种有前途的自动驾驶范式，可以利用世界知识和推理能力，尤其是在长尾场景中。然而，现有的 VLA 模型在使用自回归生成框架进行动作生成时，经常面临高延迟问题，并且表现出有限的鲁棒性。在本文中，我们提出了 SpanVLA，一个新颖的端到端自动驾驶框架，它整合了自回归推理和一个流匹配动作专家。首先，SpanVLA 引入了一种高效的桥接机制，利用视觉语言模型 (VLM) 的视觉和推理指导，通过以历史轨迹初始化为条件的流匹配策略来高效规划未来轨迹，这显著减少了推理时间。其次，为了进一步提高 SpanVLA 模型的性能和鲁棒性，我们提出了一种基于 GRPO 的后训练方法，使 VLA 模型不仅能从积极的驾驶样本中学习，还能学习如何避免典型的负面行为并学习恢复行为。我们进一步介绍了 mReasoning，一个关注复杂、需要推理的场景以及负面-恢复样本的全新真实世界驾驶推理数据集。在 NAVSIM (v1 和 v2) 上的大量实验证明了 SpanVLA 模型的竞争性性能。此外，在不同场景下的定性结果突出了我们模型的规划性能和鲁棒性。</td>
      <td style="width: 20%; vertical-align: top;">本文针对现有视觉-语言-动作 (VLA) 模型在自动驾驶中动作生成高延迟和鲁棒性不足的问题，提出了 SpanVLA 框架。该框架通过一个高效桥接机制将 VLM 的推理能力与流匹配动作专家结合，显著降低了轨迹规划的推理时间；同时，引入基于 GRPO 的后训练方法，使模型能从正面及负面恢复样本中学习，并提出了 mReasoning 数据集以强化复杂场景推理。实验结果表明 SpanVLA 在规划性能和鲁棒性上具有强大的竞争力。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>6. From Particles to Perils: SVGD-Based Hazardous Scenario Generation for Autonomous Driving Systems Testing</strong><br><span>Linfeng Liang, Xiao Cheng, Tsong Yueh Chen, Xi Zheng</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-04-20</div><div>2026-04-20</div><div><a href="http://arxiv.org/abs/2604.18918v1">2604.18918v1</a> / <a href="https://arxiv.org/pdf/2604.18918v1">PDF</a></div><div>cs.SE, cs.LG</div></td>
      <td style="width: 10%; vertical-align: top;">RL</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>自动驾驶系统（ADS）的基于仿真的测试必须在密集、异构的交通中发现真实且多样化的故障。然而，现有的基于搜索的种子生成方法（例如遗传算法）在高维空间中表现不佳，常常收敛到有限的模式并遗漏许多故障场景。我们提出了 PtoP，一个结合自适应随机种子生成和斯坦变分梯度下降（SVGD）的框架，以生成多样化、能诱发故障的初始条件。SVGD 平衡了向高风险区域的吸引力和粒子之间的排斥力，从而产生了寻求风险但又在多个故障模式中分布良好的种子。PtoP 是即插即用的，通过提供有原则的种子来增强现有的在线测试方法（例如基于强化学习的测试器）。在 CARLA 中对两个工业级 ADS（Apollo、Autoware）和一个原生端到端系统进行的评估表明，PtoP 在安全违规率（高达 27.68%）、场景多样性（9.6%）和地图覆盖率（16.78%）方面均优于基线方法。</td>
      <td style="width: 20%; vertical-align: top;">自动驾驶系统测试中，现有搜索方法在高维空间难以有效生成多样化故障场景。本文提出 PtoP 框架，结合自适应随机种子生成与斯坦变分梯度下降（SVGD），以产生多样化、能诱发故障的初始条件。实验证明，PtoP 能显著提高安全违规率、场景多样性和地图覆盖率，有效增强现有在线测试方法。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>7. Asset Harvester: Extracting 3D Assets from Autonomous Driving Logs for Simulation</strong><br><span>Tianshi Cao, Jiawei Ren, Yuxuan Zhang, Jaewoo Seo, Jiahui Huang, Shikhar Solanki, Haotian Zhang, Mingfei Guo, Haithem Turki, Muxingzi Li, Yue Zhu, Sipeng Zhang, Zan Gojcic, Sanja Fidler, Kangxue Yin</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-04-20</div><div>2026-04-20</div><div><a href="http://arxiv.org/abs/2604.18468v1">2604.18468v1</a> / <a href="https://arxiv.org/pdf/2604.18468v1">PDF</a></div><div>cs.CV, cs.AI, cs.GR, cs.LG</div></td>
      <td style="width: 10%; vertical-align: top;">distillation</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>闭环仿真作为自动驾驶车辆 (AV) 开发的核心组成部分，使得在实际部署前进行可扩展的测试、训练和安全验证成为可能。神经场景重建能将驾驶日志转换为用于仿真的交互式 3D 环境，但它无法生成代理操纵和大规模视角新视图合成所需的完整 3D 对象资产。为解决这一挑战，我们提出了 Asset Harvester，这是一个图像到 3D 模型和端到端管线，能将来自真实驾驶日志的稀疏、野外对象观测转换为完整的、可用于仿真的资产。我们没有仅仅依赖单一模型组件，而是为真实世界的 AV 数据开发了一个系统级设计，该设计结合了以对象为中心的大规模训练元组的策划、跨异构传感器的几何感知预处理，以及一个稳健的训练配方，将稀疏视图条件下的多视图生成与 3D 高斯提升相结合。在此系统内，SparseViewDiT 经过专门设计，用于解决有限角度视图和其他真实世界数据挑战。结合混合数据策划、增强和自蒸馏，该系统能够将稀疏的 AV 对象观测可扩展地转换为可重用的 3D 资产。</td>
      <td style="width: 20%; vertical-align: top;">自动驾驶车辆的闭环仿真急需完整的 3D 对象资产，但现有神经场景重建无法提供。本文提出了 Asset Harvester，一个端到端的图像到 3D 管线，能将驾驶日志中稀疏的野外对象观测转换为完整的、可用于仿真的 3D 资产。该系统通过大规模数据整理、几何感知预处理和结合稀疏视图条件多视图生成与 3D 高斯提升的稳健训练方法，实现了可扩展的 3D 资产提取。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>8. OneDrive: Unified Multi-Paradigm Driving with Vision-Language-Action Models</strong><br><span>Yiwei Zhang, Xuesong Chen, Jin Gao, Hanshi Wang, Fudong Ge, Weiming Hu, Shaoshuai Shi, Zhipeng Zhang</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-04-20</div><div>2026-04-20</div><div><a href="http://arxiv.org/abs/2604.17915v1">2604.17915v1</a> / <a href="https://arxiv.org/pdf/2604.17915v1">PDF</a></div><div>cs.CV</div></td>
      <td style="width: 10%; vertical-align: top;">VLM</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>视觉语言模型（VLM）在自回归文本生成方面表现出色，然而，端到端自动驾驶需要多任务学习，包括结构化输出和异构解码行为，例如自回归语言生成、并行目标检测和轨迹回归。为了适应这些差异，现有系统通常引入单独或级联的解码器，导致架构碎片化和骨干网络重用受限。在这项工作中，我们提出了一个基于预训练 VLM 的统一自动驾驶框架，其中异构解码行为在单个 Transformer 解码器中得到协调。我们证明了预训练 VLM 的注意力机制在纯语言建模之外表现出强大的可迁移性。通过在单个因果解码器中组织视觉和结构化查询令牌，结构化查询可以通过原始注意力机制自然地依赖视觉上下文。文本和结构化输出共享一个共同的注意力骨干网络，从而实现异构任务之间的稳定联合优化。轨迹规划通过引入结构化轨迹查询在同一因果 LLM 解码器中实现。这种统一的公式使得规划能够与图像和感知令牌共享预训练的注意力骨干网络。在端到端自动驾驶基准测试中进行的广泛实验证明了最先进的性能，包括 nuScenes 开放循环评估中的 0.28 L2 和 0.18 碰撞率，以及 NAVSIM 闭环评估中的竞争性结果（86.8 PDMS）。完整模型保留了多模态生成能力，而高效推理模式将延迟降低了约 40%。代码和模型可在 https://github.com/Z1zyw/OneDrive 获取。</td>
      <td style="width: 20%; vertical-align: top;">该论文提出了一个名为 OneDrive 的统一自动驾驶框架，它基于预训练的视觉语言模型（VLM）。该框架通过在一个 Transformer 解码器中整合不同的解码行为，解决了现有系统因使用独立解码器而导致的架构碎片化问题。OneDrive 证明了预训练 VLM 的注意力机制在自动驾驶任务中具有很强的迁移能力，并在 nuScenes 和 NAVSIM 等端到端自动驾驶基准测试中取得了最先进的性能。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>9. Infrastructure-Centric World Models: Bridging Temporal Depth and Spatial Breadth for Roadside Perception</strong><br><span>Siyuan Meng, Chengbo Ai</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-04-19</div><div>2026-04-19</div><div><a href="http://arxiv.org/abs/2604.17651v1">2604.17651v1</a> / <a href="https://arxiv.org/pdf/2604.17651v1">PDF</a></div><div>cs.CV, cs.RO</div></td>
      <td style="width: 10%; vertical-align: top;">world model</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>世界模型，即模拟环境演变方式的生成式AI系统，正在彻底改变自动驾驶领域，然而所有现有方法都采用以自我车辆为中心的视角，而忽略了基础设施视角。我们认为，以基础设施为中心的世界模型提供了一种根本上互补的能力：路侧系统独有的鸟瞰、多传感器、持久的视角。我们论点核心是时空互补性：固定的路侧传感器擅长时间深度，能够积累包括罕见安全关键事件在内的长期行为分布，而车载传感器擅长空间广度，可以在大型道路网络中采样多样化的场景。本文提出了一个分为三个阶段的以基础设施为中心的世界模型（I-WM）愿景：(I) 具有质量感知不确定性传播的生成式场景理解，(II) 具有多智能体反事实推理的物理感知预测动力学，以及 (III) 通过潜在空间对齐实现V2X通信的协作世界模型。我们提出了一种双层架构，将无标注感知作为多模态数据引擎，为端到端生成式世界模型提供数据，并采用从激光雷达到4D雷达、信号相位数据再到事件相机的分阶段传感器策略。我们建立了驾驶世界模型范式的分类体系，将I-WM置于LeCun的JEPA、李飞飞的空间智能和VLA架构的背景下进行定位，并引入基础设施VLA（I-VLA）作为路侧感知、语言指令和交通控制行动的新型统一体。我们的愿景建立在现有多激光雷达管道之上，并确定了每个阶段的开源基础，为实现能够理解和预测交通的基础设施提供了一条途径。</td>
      <td style="width: 20%; vertical-align: top;">当前自动驾驶世界模型主要以车载视角为主，忽略了基础设施视角。本文提出了一种以基础设施为中心的世界模型（I-WM）愿景，利用路侧系统的鸟瞰、多传感器优势，实现时空互补的生成式场景理解和预测动力学。通过双层架构和分阶段传感器策略，该研究旨在构建能够理解并预测交通的基础设施，并引入基础设施VLA（I-VLA）统一路侧感知、语言指令和交通控制。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>10. Beyond Conservative Automated Driving in Multi-Agent Scenarios via Coupled Model Predictive Control and Deep Reinforcement Learning</strong><br><span>Saeed Rahmani, Gözde Körpe, Zhenlin, Xu, Bruno Brito, Simeon Craig Calvert, Bart van Arem</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-04-15</div><div>2026-04-15</div><div><a href="http://arxiv.org/abs/2604.13891v1">2604.13891v1</a> / <a href="https://arxiv.org/pdf/2604.13891v1">PDF</a></div><div>cs.RO, cs.AI, eess.SY</div></td>
      <td style="width: 10%; vertical-align: top;">RL</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>无信号灯交叉路口的自动驾驶具有挑战性，原因在于复杂的车辆间交互以及需要在安全性和效率之间取得平衡。模型预测控制 (MPC) 通过优化提供结构化的约束处理，但它依赖于手工设计的规则，这些规则通常会产生过于保守的行为。深度强化学习 (RL) 从经验中学习适应性行为，但通常在安全保障和对未见环境的泛化方面遇到困难。在本研究中，我们提出了一种集成的 MPC-RL 框架，以提高多智能体场景中的导航性能。实验表明，MPC-RL 在三种交通密度水平下均优于独立的 MPC 和端到端 RL。总体而言，与纯 MPC 相比，MPC-RL 将碰撞率降低了 21%，成功率提高了 6.5%。我们进一步评估了在不重新训练的情况下对高速公路合并场景进行零样本迁移。基于 MPC 的方法都比端到端 PPO 具有更好的迁移能力，这突出了 MPC 主干在跨场景鲁棒性中的作用。该框架在训练期间还显示出比端到端 RL 更快的损失稳定速度，这表明学习负担有所减轻。这些结果表明，该集成方法可以在多智能体交叉路口场景中改善安全性能和效率之间的平衡，同时 MPC 组件为跨驾驶环境的泛化提供了坚实的基础。实施代码已开源。</td>
      <td style="width: 20%; vertical-align: top;">本研究旨在解决无信号灯交叉路口自动驾驶中安全性与效率难以平衡的问题，指出传统 MPC 过于保守而纯 RL 缺乏安全保障和泛化能力。作者提出了一种集成的 MPC-RL 框架，以结合两者的优势。实验结果表明，该框架在多智能体场景下显著优于独立 MPC 和端到端 RL，不仅降低了碰撞率并提高了成功率，还展示了更好的跨场景泛化能力和更快的训练收敛速度。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>11. Learning Vision-Language-Action World Models for Autonomous Driving</strong><br><span>Guoqing Wang, Pin Tang, Xiangxuan Ren, Guodongfang Zhao, Bailan Feng, Chao Ma</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-04-10</div><div>2026-04-10</div><div><a href="http://arxiv.org/abs/2604.09059v1">2604.09059v1</a> / <a href="https://arxiv.org/pdf/2604.09059v1">PDF</a></div><div>cs.CV, cs.AI</div></td>
      <td style="width: 10%; vertical-align: top;">world model, RL</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>视觉-语言-动作 (VLA) 模型最近在端到端自动驾驶领域取得了显著进展，它将感知、推理和控制集成到统一的多模态框架中。然而，它们通常缺乏对时间动态和全局世界一致性的明确建模，这限制了它们的预见性和安全性。相比之下，世界模型可以模拟合理的未来场景，但通常难以对其生成的想象未来进行推理或评估。在这项工作中，我们提出了 VLA-World，一个简单而有效的 VLA 世界模型，它将预测性想象与反思性推理相结合，以提高驾驶预见性。VLA-World 首先利用动作衍生的可行轨迹来指导下一帧图像的生成，捕获描述周围环境如何演变的丰富的空间和时间线索。然后，模型对这个自我生成的未来想象帧进行推理，以完善预测轨迹，从而实现更高的性能和更好的可解释性。为了支持这一流程，我们整理了 nuScenes-GR-20K，一个源自 nuScenes 的生成式推理数据集，并采用了包括预训练、监督微调和强化学习在内的三阶段训练策略。大量实验表明，VLA-World 在规划和未来生成基准测试中，始终超越了最先进的 VLA 和世界模型基线。项目页面：https://vlaworld.github.io</td>
      <td style="width: 20%; vertical-align: top;">现有端到端自动驾驶VLA模型缺乏时间动态和全局一致性建模，限制了其预见性，而世界模型虽能模拟未来但难以推理。本文提出VLA-World，一个结合预测性想象和反思性推理的VLA世界模型，它利用动作轨迹指导未来场景生成，再对生成结果进行推理以优化预测轨迹。该模型显著提升了自动驾驶的预见性、性能和可解释性，并在规划和未来生成任务上超越了当前先进基线。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>12. LMGenDrive: Bridging Multimodal Understanding and Generative World Modeling for End-to-End Driving</strong><br><span>Hao Shao, Letian Wang, Yang Zhou, Yuxuan Hu, Zhuofan Zong, Steven L. Waslander, Wei Zhan, Hongsheng Li</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-04-09</div><div>2026-04-09</div><div><a href="http://arxiv.org/abs/2604.08719v1">2604.08719v1</a> / <a href="https://arxiv.org/pdf/2604.08719v1">PDF</a></div><div>cs.CV, cs.AI, cs.RO</div></td>
      <td style="width: 10%; vertical-align: top;">VLM, world model</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>近年来，自动驾驶取得了显著进展，但泛化到长尾和开放世界场景仍然是大规模部署的主要瓶颈。为应对这一挑战，一些研究利用大型语言模型（LLMs）和视觉语言模型（VLMs）进行视觉-语言理解和推理，使车辆在生成动作时能够解释罕见和安全关键的情境。另一些研究则探索生成式世界模型，以捕捉驾驶场景的时空演变，使智能体能够在行动前设想可能的未来。受人类智能统一理解和想象的启发，我们探索了一种用于自动驾驶的统一模型。我们提出了LMGenDrive，这是第一个将基于LLM的多模态理解与生成式世界模型相结合，实现端到端闭环驾驶的框架。鉴于多视角摄像头输入和自然语言指令，LMGenDrive能够生成未来的驾驶视频和控制信号。这种设计提供了互补的优势：视频预测改善了时空场景建模，而LLM则从大规模预训练中贡献了强大的语义先验和指令基础。我们进一步提出了一种渐进式三阶段训练策略，从视觉预训练到多步长时程驾驶，以提高稳定性和性能。LMGenDrive支持低延迟在线规划和自回归离线视频生成。实验表明，它在具有挑战性的闭环基准测试中显著优于现有方法，在指令遵循、时空理解以及对罕见场景的鲁棒性方面均有明显提升。这些结果表明，统一多模态理解和生成是实现更具泛化性和鲁棒性的具身决策系统的一个有前景的方向。</td>
      <td style="width: 20%; vertical-align: top;">本文旨在解决自动驾驶在长尾和开放世界场景中泛化能力不足的问题，通过统一理解与想象来提升性能。作者提出了LMGenDrive框架，它首次将基于LLM的多模态理解与生成式世界模型相结合，用于端到端闭环驾驶，能够同时生成未来驾驶视频和控制信号。实验结果表明，LMGenDrive在指令遵循、时空理解和罕见场景的鲁棒性方面显著优于现有方法，为实现更具泛化性和鲁棒性的自动驾驶系统提供了新方向。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>13. Fuzzy Encoding-Decoding to Improve Spiking Q-Learning Performance in Autonomous Driving</strong><br><span>Aref Ghoreishee, Abhishek Mishra, Lifeng Zhou, John Walsh, Anup Das, Nagarajan Kandasamy</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-04-06</div><div>2026-04-06</div><div><a href="http://arxiv.org/abs/2604.16436v1">2604.16436v1</a> / <a href="https://arxiv.org/pdf/2604.16436v1">PDF</a></div><div>cs.NE, cs.LG</div></td>
      <td style="width: 10%; vertical-align: top;">RL</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>本文开发了一种端到端的模糊编码-解码架构，用于增强自动驾驶中基于视觉的多模态深度脉冲Q网络。该方法解决了脉冲强化学习的两个核心局限性：一是密集视觉输入转换为稀疏脉冲序列导致的信息损失，二是基于脉冲的价值函数表示能力有限，这通常导致Q值估计的区分度较弱。编码器引入了可训练的模糊隶属函数来生成富有表现力的、基于种群的脉冲表示，解码器则使用轻量级神经解码器从脉冲输出中重建连续的Q值。在HighwayEnv基准上的实验表明，所提出的架构显著提高了决策准确性，并缩小了脉冲与非脉冲多模态Q网络之间的性能差距。结果突出了该框架在利用脉冲神经网络实现高效实时自动驾驶方面的潜力。</td>
      <td style="width: 20%; vertical-align: top;">这篇论文解决了脉冲强化学习在自动驾驶中面临的信息损失和Q值区分度不足的问题。研究人员提出了一种端到端的模糊编码-解码架构，通过模糊隶属函数生成丰富的脉冲表示，并利用神经解码器重建连续Q值。实验结果表明，该方法显著提升了决策准确性，缩小了脉冲与非脉冲Q网络间的性能差距，展现了其在高效实时自动驾驶中的潜力。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>14. HAD: Combining Hierarchical Diffusion with Metric-Decoupled RL for End-to-End Driving</strong><br><span>Wenhao Yao, Xinglong Sun, Zhenxin Li, Shiyi Lan, Zi Wang, Jose M. Alvarez, Zuxuan Wu</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-04-04</div><div>2026-04-04</div><div><a href="http://arxiv.org/abs/2604.03581v1">2604.03581v1</a> / <a href="https://arxiv.org/pdf/2604.03581v1">PDF</a></div><div>cs.RO, cs.CV</div></td>
      <td style="width: 10%; vertical-align: top;">RL</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>端到端规划已成为自动驾驶的主导范式，其中最近的模型通常采用评分-选择框架从大量候选轨迹中进行选择，而基于扩散的解码显示出强大的前景。然而，直接从整个候选空间中选择仍然难以优化，并且扩散中使用的 Gaussian 扰动常常引入不切实际的轨迹，从而使去噪过程复杂化。此外，为了训练这些模型，强化学习 (RL) 显示出前景，但现有的端到端 RL 方法通常依赖于没有结构化信号的单一耦合奖励，从而限制了优化效率。为了解决这些挑战，我们提出了 HAD，一个具有分层扩散策略的端到端规划框架，它将规划分解为从粗到精的过程。为了改进轨迹生成，我们引入了结构保持轨迹扩展，它在保持运动学结构的同时生成真实的候选轨迹。为了策略学习，我们开发了度量解耦策略优化 (MDPO)，以实现跨多个驾驶目标的结构化 RL 优化。大量实验表明，HAD 在 NAVSIM 和 HUGSIM 上均实现了新的最先进性能，以巨大的优势超越了现有技术：NAVSIM 上提高了 +2.3 EPDMS，HUGSIM 上提高了 +4.9 路线完成度。</td>
      <td style="width: 20%; vertical-align: top;">本研究旨在解决自动驾驶端到端规划中轨迹选择优化困难、扩散模型生成非真实轨迹以及强化学习奖励耦合导致的优化效率低下等问题。为此，论文提出了 HAD 框架，结合分层扩散策略以粗到精的方式进行规划，并利用结构保持轨迹扩展生成真实轨迹，同时采用度量解耦策略优化实现多目标强化学习。实验证明，HAD 在 NAVSIM 和 HUGSIM 数据集上均达到了最先进的性能，显著优于现有方法。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>15. ExploreVLA: Dense World Modeling and Exploration for End-to-End Autonomous Driving</strong><br><span>Zihao Sheng, Xin Ye, Jingru Luo, Sikai Chen, Liu Ren</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-04-03</div><div>2026-04-03</div><div><a href="http://arxiv.org/abs/2604.02714v1">2604.02714v1</a> / <a href="https://arxiv.org/pdf/2604.02714v1">PDF</a></div><div>cs.CV</div></td>
      <td style="width: 10%; vertical-align: top;">world model, RL</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>基于视觉-语言-动作（VLA）架构的端到端自动驾驶模型通过在专家演示上进行行为克隆学习驾驶策略，已显示出有希望的结果。然而，模仿学习固有地将模型限制在复制观察到的行为，而无法探索多样化的驾驶策略，使其在新颖或分布外场景中表现脆弱。强化学习（RL）通过实现超越专家分布的策略探索，提供了一种自然的补救方法。然而，VLA模型通常在离线数据集上训练，缺乏直接可观察的状态转换，因此需要一个学习到的世界模型来预测动作后果。在这项工作中，我们提出了一个统一的理解-生成框架，该框架利用世界建模同时实现有意义的探索并提供密集监督。具体来说，我们将轨迹预测与未来RGB和深度图像生成相结合，作为密集世界建模目标，要求模型学习细粒度的视觉和几何表示，从而极大地丰富规划主干。除了作为监督信号外，世界模型还充当策略探索的内在奖励来源：其图像预测不确定性自然地衡量轨迹相对于训练分布的新颖性，其中高不确定性表示分布外场景，如果安全，则代表有价值的学习机会。我们将这种探索信号整合到一个安全门控奖励中，并通过群组相对策略优化（GRPO）来优化策略。在NAVSIM和nuScenes基准测试上的实验证明了我们方法的有效性，在NAVSIM上实现了93.7的PDMS分数和88.8的EPDMS分数，达到了最先进水平。代码和演示将在 https://zihaosheng.github.io/ExploreVLA/ 公开提供。</td>
      <td style="width: 20%; vertical-align: top;">针对端到端VLA自动驾驶模型在陌生场景中探索不足的问题，本文提出了ExploreVLA框架。该框架利用密集世界模型预测未来的RGB和深度图像，从而提供丰富的视觉几何表示进行规划，并以预测不确定性作为内在奖励来指导安全探索。实验表明，ExploreVLA在NAVSIM和nuScenes基准测试上实现了最先进的性能。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>16. $AutoDrive\text{-}P^3$: Unified Chain of Perception-Prediction-Planning Thought via Reinforcement Fine-Tuning</strong><br><span>Yuqi Ye, Zijian Zhang, Junhong Lin, Shangkun Sun, Changhao Peng, Wei Gao</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-03-30</div><div>2026-03-30</div><div><a href="http://arxiv.org/abs/2603.28116v1">2603.28116v1</a> / <a href="https://arxiv.org/pdf/2603.28116v1">PDF</a></div><div>cs.RO, cs.CV</div></td>
      <td style="width: 10%; vertical-align: top;">VLM, RL</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>视觉语言模型（VLM）因其在处理长尾场景方面的卓越表现，正越来越多地被采用于端到端自动驾驶系统。然而，当前基于VLM的方法存在两个主要局限性：1）一些VLM直接输出规划结果，没有经过思维链（CoT）推理，绕过了关键的感知和预测阶段，这产生了显著的领域差距并损害了决策能力；2）其他VLM可以为感知、预测和规划任务生成输出，但采用的是碎片化的决策方法，这些模块独立运行，导致协同作用严重缺乏，从而削弱了真正的规划性能。为了解决这些局限性，我们提出了${AutoDrive\text{-}P^3}$，一个通过结构化推理无缝整合\textbf{感知}、\textbf{预测}和\textbf{规划}的新颖框架。我们引入了${P^3\text{-}CoT}$数据集以促进连贯推理，并提出了${P^3\text{-}GRPO}$，一种分层强化学习算法，为所有三个任务提供渐进式监督。具体而言，${AutoDrive\text{-}P^3}$逐步生成感知、预测和规划的CoT推理和答案，其中感知为后续的预测和规划提供基本信息，而感知和预测共同为最终的规划决策做出贡献，从而实现更安全、更可解释的自动驾驶。此外，为了平衡推理效率和性能，我们引入了双重思维模式：详细思维和快速思维。在开环（nuScenes）和闭环（NAVSIMv1/v2）基准上进行的广泛实验表明，我们的方法在规划任务中取得了最先进的性能。代码可在https://github.com/haha-yuki-haha/AutoDrive-P3获取。</td>
      <td style="width: 20%; vertical-align: top;">当前基于视觉语言模型的自动驾驶系统存在思维链缺失或感知-预测-规划模块协同不足的问题。为解决此，${AutoDrive\text{-}P^3}$框架通过结构化推理无缝整合感知、预测和规划，并引入${P^3\text{-}CoT}$数据集和分层强化学习算法${P^3\text{-}GRPO}$以实现协同决策。该方法通过逐步生成思维链推理，实现了更安全、可解释的自动驾驶，并在多个基准测试中展现出最先进的规划性能。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>17. Collision-Aware Vision-Language Learning for End-to-End Driving with Multimodal Infraction Datasets</strong><br><span>Alex Koran, Dimitrios Sinodinos, Hadi Hojjati, Takuya Nanri, Fangge Chen, Narges Armanfard</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-03-26</div><div>2026-03-26</div><div><a href="http://arxiv.org/abs/2603.25946v1">2603.25946v1</a> / <a href="https://arxiv.org/pdf/2603.25946v1">PDF</a></div><div>cs.CV, cs.AI, cs.LG</div></td>
      <td style="width: 10%; vertical-align: top;">VLM</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>高违规率仍然是端到端（E2E）自动驾驶的主要瓶颈，这在CARLA排行榜上的低驾驶分数中得到了体现。尽管与碰撞相关的违规是闭环评估中的主要故障模式，但碰撞感知表征学习受到的关注有限。为了解决这一空白，我们首先开发了一个视频-语言增强异常检测器（VLAAD），它利用多实例学习（MIL）公式来获取稳定、时间局部化的碰撞信号，用于主动预测。为了将这些能力转化到闭环模拟中，我们必须克服现有模拟器数据集的局限性，这些数据集缺乏多模态性，并且经常局限于简单的交叉路口场景。因此，我们引入了CARLA-Collide，这是一个大规模多模态数据集，用于捕获高度多样化路网中的真实碰撞事件。在这些多样化的模拟器数据上进行训练后，VLAAD可作为一个碰撞感知插件模块，无缝集成到现有的E2E驾驶模型中。通过将我们的模块集成到预训练的TransFuser++代理中，我们证明了在最小微调的情况下，驾驶分数相对提高了14.12%。除了闭环评估，我们还使用真实世界的驾驶数据在开环设置中进一步评估了VLAAD的泛化能力。为了支持这项分析，我们引入了Real-Collide，这是一个多模态数据集，包含多样化的行车记录仪视频，并配有语义丰富的碰撞检测和预测注释。在此基准上，尽管VLAAD仅包含0.6亿参数，但它超越了一个多亿参数的视觉-语言模型，在AUC方面实现了23.3%的改进。</td>
      <td style="width: 20%; vertical-align: top;">端到端自动驾驶面临高违规率（尤其是碰撞）瓶颈，而碰撞感知学习不足。本文提出VLAAD（视频-语言增强异常检测器），利用多实例学习实现主动碰撞预测，并构建了CARLA-Collide和Real-Collide两个多模态数据集。VLAAD作为一个可插拔模块，能显著提升现有E2E驾驶模型的驾驶分数（相对提高14.12%），并在真实世界数据上展现出优异的泛化能力，超越了参数量更大的视觉-语言模型。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>18. COIN: Collaborative Interaction-Aware Multi-Agent Reinforcement Learning for Self-Driving Systems</strong><br><span>Yifeng Zhang, Jieming Chen, Tingguang Zhou, Tanishq Duhan, Jianghong Dong, Yuhong Cao, Guillaume Sartoretti</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-03-26</div><div>2026-03-26</div><div><a href="http://arxiv.org/abs/2603.24931v1">2603.24931v1</a> / <a href="https://arxiv.org/pdf/2603.24931v1">PDF</a></div><div>cs.RO</div></td>
      <td style="width: 10%; vertical-align: top;">RL</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>多智能体自动驾驶（MASD）系统为协调自动驾驶车辆提供了一种有效的解决方案，旨在未来智能交通系统中减少拥堵，并提高安全性和运营效率。多智能体强化学习（MARL）已成为开发先进的端到端MASD系统的一种有前途的方法。然而，在具有复杂智能体交互的密集场景中，实现动态MASD系统中的高效安全协作仍然是一个重大挑战。为了解决这一挑战，我们提出了一种新颖的协作式（CO-）交互感知（-IN）MARL框架，命名为COIN。具体来说，我们开发了一种新的反事实个体-全局双延迟深度确定性策略梯度（CIG-TD3）算法，该算法以“集中式训练、分布式执行”（CTDE）方式精心设计，旨在共同优化智能体的个体目标（导航）和全局目标（协作）。我们进一步引入了一种双层交互感知集中式评论家架构，该架构捕获了局部成对交互和全局系统级依赖关系，从而实现了更准确的全局价值估计和改进的信用分配，以促进协作策略学习。我们在密集的城市交通环境中进行了广泛的仿真实验，结果表明，COIN在各种系统规模下，在安全性和效率方面始终优于其他先进的基线方法。这些结果突显了其在复杂动态MASD场景中的优越性，并通过真实世界机器人演示得到了进一步验证。补充视频可在 https://marmotlab.github.io/COIN/ 查看。</td>
      <td style="width: 20%; vertical-align: top;">针对多智能体自动驾驶系统在复杂密集场景中实现高效安全协作的挑战，本文提出了COIN框架。该框架引入了CIG-TD3算法来同时优化智能体的个体和全局目标，并设计了双层交互感知集中式评论家架构以捕捉多层次交互。实验结果表明，COIN在安全性和效率方面均优于现有方法，验证了其在复杂MASD场景中的有效性。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>19. Latent-WAM: Latent World Action Modeling for End-to-End Autonomous Driving</strong><br><span>Linbo Wang, Yupeng Zheng, Qiang Chen, Shiwei Li, Yichen Zhang, Zebin Xing, Qichao Zhang, Xiang Li, Deheng Qian, Pengxuan Yang, Yihang Dong, Ce Hao, Xiaoqing Ye, Junyu han, Yifeng Pan, Dongbin Zhao</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-03-25</div><div>2026-03-25</div><div><a href="http://arxiv.org/abs/2603.24581v1">2603.24581v1</a> / <a href="https://arxiv.org/pdf/2603.24581v1">PDF</a></div><div>cs.CV, cs.RO</div></td>
      <td style="width: 10%; vertical-align: top;">world model</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>我们引入了Latent-WAM，这是一种高效的端到端自动驾驶框架，它通过空间感知和动态信息丰富的潜在世界表示实现强大的轨迹规划。现有的基于世界模型的规划器存在表示压缩不足、空间理解有限以及时间动态利用不足的问题，导致在受限的数据和计算预算下规划效果不佳。Latent-WAM通过两个核心模块解决了这些局限性：一个空间感知压缩世界编码器（SCWE），它从基础模型中提取几何知识，并通过可学习查询将多视图图像压缩为紧凑的场景令牌；以及一个动态潜在世界模型（DLWM），它采用因果Transformer，根据历史视觉和运动表示自回归地预测未来世界状态。在NAVSIM v2和HUGSIM上进行的大量实验表明，该方法取得了新的最先进结果：在NAVSIM v2上达到89.3 EPDMS，在HUGSIM上达到28.9 HD-Score，以显著更少的训练数据和紧凑的104M参数模型，超越了之前最佳的无感知方法3.2 EPDMS。</td>
      <td style="width: 20%; vertical-align: top;">本文介绍了Latent-WAM，一个用于端到端自动驾驶的框架，旨在解决现有世界模型在表示压缩、空间理解和时间动态方面的不足。它通过空间感知压缩世界编码器（SCWE）和动态潜在世界模型（DLWM）实现高效的轨迹规划。该方法在NAVSIM v2和HUGSIM上取得了最先进的成果，验证了其在数据和计算效率上的优越性。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>20. LongTail Driving Scenarios with Reasoning Traces: The KITScenes LongTail Dataset</strong><br><span>Royden Wagner, Omer Sahin Tas, Jaime Villa, Felix Hauser, Yinzhe Shen, Marlon Steiner, Dominik Strutz, Carlos Fernandez, Christian Kinzig, Guillermo S. Guitierrez-Cabello, Hendrik Königshof, Fabian Immel, Richard Schwarzkopf, Nils Alexander Rack, Kevin Rösch, Kaiwen Wang, Jan-Hendrik Pauls, Martin Lauer, Igor Gilitschenski, Holger Caesar, Christoph Stiller</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-03-24</div><div>2026-04-06</div><div><a href="http://arxiv.org/abs/2603.23607v2">2603.23607v2</a> / <a href="https://arxiv.org/pdf/2603.23607v2">PDF</a></div><div>cs.CV, cs.RO</div></td>
      <td style="width: 10%; vertical-align: top;">VLM</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>在自动驾驶等现实世界领域中，对罕见场景的泛化仍然是一个基本挑战。为了解决这个问题，我们引入了一个新的数据集，专为端到端驾驶设计，侧重于长尾驾驶事件。我们提供多视角视频数据、轨迹、高级指令和详细的推理轨迹，以促进上下文学习和少样本泛化。这个为多模态模型（如VLM和VLA）提供的基准测试，通过评估指令遵循和模型输出之间的语义连贯性，超越了安全和舒适性指标。英文、西班牙文和中文的多语言推理轨迹来自具有不同文化背景的领域专家。因此，我们的数据集是研究不同形式的推理如何影响驾驶能力的独特资源。我们的数据集可在：https://hf.co/datasets/kit-mrt/kitscenes-longtail 获取。</td>
      <td style="width: 20%; vertical-align: top;">自动驾驶在罕见场景的泛化能力上存在挑战。为解决此问题，本文推出了KITScenes LongTail数据集，专注于长尾驾驶事件，并提供多视角视频、轨迹、高级指令及多语言推理轨迹。该数据集为多模态模型提供了一个新的基准，通过评估指令遵循和语义连贯性来衡量驾驶能力，并可用于研究不同推理形式对驾驶能力的影响。</td>
    </tr>
  </tbody>
</table>
