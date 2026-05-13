# arXiv 自动驾驶论文

Generated: 2026-05-13 21:20 UTC

当前展示 100 篇论文的最新版本。旧版本只保留 arXiv 链接。

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
      <td style="width: 23%; vertical-align: top;"><strong>1. DeepSight: Long-Horizon World Modeling via Latent States Prediction for End-to-End Autonomous Driving</strong><br><span>Lingjun Zhang, Changjie Wu, Linzhe Shi, Jiangyang Li, Jiaxin Liu, Lei Yang, Hang Zhang, Mu Xu, Hong Wang</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-05-11</div><div>2026-05-11</div><div><a href="http://arxiv.org/abs/2605.10564v1">2605.10564v1</a> / <a href="https://arxiv.org/pdf/2605.10564v1">PDF</a></div><div>cs.CV, cs.RO</div></td>
      <td style="width: 10%; vertical-align: top;">VLM, world model</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>端到端自动驾驶系统正越来越多地整合视觉-语言模型（VLM）架构，通过引入文本推理或视觉推理来增强驾驶决策的鲁棒性和准确性。然而，大多数方法中采用的推理机制是从通用领域直接改编而来，缺乏针对自动驾驶场景的深入探索，尤其是在视觉推理模块内部。在本文中，我们提出了一种驾驶世界模型，该模型在鸟瞰图（BEV）空间中对连续未来帧的潜在语义特征进行并行预测，从而实现了未来世界状态的长期建模。我们还引入了一种高效且自适应的文本推理机制，该机制利用额外的社会知识和推理能力，进一步改善了在具有挑战性的长尾场景中的驾驶性能。我们提出了一种新颖、高效且有效的方法，并在闭环Bench2drive基准测试中取得了最先进（SOTA）的结果。</td>
      <td style="width: 20%; vertical-align: top;">当前端到端自动驾驶系统中的推理机制缺乏针对驾驶场景的深入定制。本文提出了一种驾驶世界模型，通过在鸟瞰图（BEV）空间中并行预测未来帧的潜在语义特征，实现长期世界状态建模。此外，还引入了高效自适应的文本推理机制来应对长尾场景，该方法在闭环Bench2drive基准测试中取得了最先进的成果。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>2. CoWorld-VLA: Thinking in a Multi-Expert World Model for Autonomous Driving</strong><br><span>Minqing Huang, Yujiao Xiang, Zihan Liang, Jiajie Huang, Jingqi Wang, Zhi Xu, Feiyang Tan, Hangning Zhou, Mu Yang, Gong Che</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-05-11</div><div>2026-05-11</div><div><a href="http://arxiv.org/abs/2605.10426v1">2605.10426v1</a> / <a href="https://arxiv.org/pdf/2605.10426v1">PDF</a></div><div>cs.CV, cs.AI</div></td>
      <td style="width: 10%; vertical-align: top;">world model</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>视觉-语言-动作 (VLA) 模型已成为端到端自动驾驶的一种有前景的范式。然而，现有的推理机制在提供面向规划的中间表示方面仍面临困难：文本链式思考 (CoT) 无法保留连续的时空结构，而潜在世界推理则难以直接用作动作生成的条件。在本文中，我们提出了 CoWorld-VLA，一个用于自动驾驶的多专家世界推理框架，其中世界表示作为显式条件来指导动作规划。CoWorld-VLA 通过多源监督提取互补的世界信息，并将其编码为 VLA 中的专家令牌，从而提供规划器可访问的条件信号。具体来说，我们构建了四种类型的令牌：语义交互、几何结构、动态演变和自我轨迹令牌，它们分别建模交互意图、空间结构、未来时间动态和行为目标。在动作生成过程中，CoWorld-VLA 采用基于扩散的分层多专家融合规划器，该规划器在整个联合去噪过程中与场景上下文耦合，以生成连续的自我轨迹。实验表明，CoWorld-VLA 在 NAVSIM v1 基准测试中在未来场景生成和规划方面都取得了有竞争力的结果，展示了在避免碰撞和轨迹精度方面的强大性能。消融研究进一步验证了专家令牌的互补性及其作为动作生成规划条件的有效性。代码将发布于 https://github.com/potatochip1211/CoWorld-VLA。</td>
      <td style="width: 20%; vertical-align: top;">针对现有自动驾驶VLA模型在生成面向规划的中间表示上的不足，本文提出了CoWorld-VLA，一个多专家世界推理框架。该方法通过多源监督提取互补世界信息并编码为四种专家令牌，再利用基于扩散的分层规划器以这些令牌为显式条件生成连续轨迹。CoWorld-VLA在NAVSIM v1基准测试中展现出在未来场景生成和规划方面具有竞争力的结果，尤其在避免碰撞和轨迹精度上表现出色。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>3. MTA-RL: Robust Urban Driving via Multi-modal Transformer-based 3D Affordances and Reinforcement Learning</strong><br><span>Guangli Chen, Dianzhao Li, Wenjian Zhong, Bangquan Xie, Ostap Okhrin</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-05-11</div><div>2026-05-11</div><div><a href="http://arxiv.org/abs/2605.10177v1">2605.10177v1</a> / <a href="https://arxiv.org/pdf/2605.10177v1">PDF</a></div><div>cs.CV, cs.AI, cs.RO</div></td>
      <td style="width: 10%; vertical-align: top;">RL</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>鲁棒的城市自动驾驶需要在密集的交互下实现可靠的3D场景理解和稳定的决策。然而，现有的端到端模型缺乏可解释性，而模块化流水线则面临脆弱接口间的误差传播问题。本文提出了MTA-RL，这是首个通过多模态基于Transformer的3D可供性（Affordances）和强化学习（RL）来连接感知与控制的框架。与之前直接回归动作的融合模型不同，MTA-RL使用Transformer架构融合RGB图像和LiDAR点云，以预测显式、几何感知的可供性表示。这些结构化表示作为紧凑的观测空间，使得强化学习策略能够纯粹基于预测的驾驶语义进行操作，从而显著提高了样本效率和稳定性。在CARLA Town01-03中，对不同交通密度（20-60辆背景车辆）进行的广泛评估表明，MTA-RL持续优于最先进的基线方法。我们的方法仅在Town03上进行训练，但在未见过的城镇中表现出卓越的零样本泛化能力，将路线完成度提高了9.0%，总距离增加了11.0%，并且将每次违规行驶距离改善了83.7%。此外，消融研究证实，我们的多模态融合和奖励塑形至关重要，显著优于仅使用图像和未塑形的变体，证明了MTA-RL在鲁棒城市自动驾驶中的有效性。</td>
      <td style="width: 20%; vertical-align: top;">现有的城市自动驾驶模型在可解释性和误差传播方面面临挑战。本文提出MTA-RL框架，通过多模态Transformer融合RGB图像和LiDAR点云，预测几何感知的3D可供性表示，并将其作为强化学习策略的紧凑观测空间。实验证明，MTA-RL在CARLA环境中显著优于现有方法，并在未见城镇中展现出卓越的零样本泛化能力，有效提升了鲁棒城市自动驾驶的表现。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>4. DriveFuture: Future-Aware Latent World Models for Autonomous Driving</strong><br><span>Yufeng Hong, Xiaotian Zhou, Yingyan Li, Xiangpo Zhou, Lin Liu, Yadan Luo, Shaoqing Xu, Lei Yang, Ziying Song</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-05-10</div><div>2026-05-10</div><div><a href="http://arxiv.org/abs/2605.09701v1">2605.09701v1</a> / <a href="https://arxiv.org/pdf/2605.09701v1">PDF</a></div><div>cs.CV</div></td>
      <td style="width: 10%; vertical-align: top;">world model</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>现有的自动驾驶潜在世界模型为面向未来的驾驶智能开辟了一条有前景的道路。然而，它们通常将未来潜在状态视为预测目标或辅助信号，而不是直接作为轨迹规划的条件。这可能会使潜在空间中的当前和未来特征纠缠不清。在这项工作中，我们提出了 DriveFuture，一个面向未来的自动驾驶潜在世界建模框架，它通过将当前潜在状态建模过程以未来世界状态为条件，明确学习面向规划的预见性。具体而言，在训练期间，模型首先从当前潜在状态和自我行动中预测未来潜在世界状态，然后通过交叉注意力根据真实未来潜在状态对预测进行修正。由此产生的面向未来的潜在状态作为基于扩散的轨迹规划器的明确条件。在推理期间，DriveFuture 以预测的未来潜在状态为条件，而不是真实未来状态。DriveFuture 在公共 NAVSIM 基准测试中取得了最先进的性能，在 NAVSIM-v2 navhard 上达到了 55.5 EPDMS，在 NAVSIM-v2 navtest 上达到了 89.9 EPDMS，在 NAVSIM-v1 navtest 上达到了 90.7 PDMS。这些结果表明，潜在世界建模的关键不仅在于模拟未来状态，更重要的是在于将当前的决策建立在未来状态的条件下。值得注意的是，截至 2026 年 4 月，DriveFuture 在 NAVSIM-v2 navhard 排行榜上排名第一，并在 NAVSIM-v1 navtest 上取得了最先进的性能。</td>
      <td style="width: 20%; vertical-align: top;">现有的自动驾驶潜在世界模型未能直接将未来潜在状态用于轨迹规划，导致特征纠缠。本文提出了 DriveFuture 框架，通过让当前潜在状态建模以未来世界状态为条件，明确学习面向规划的预见性。该方法在 NAVSIM 基准测试中取得了最先进的性能，强调了将当前决策与未来状态结合的重要性。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>5. See Tomorrow, Act Today: Foresight-Driven Autonomous Driving</strong><br><span>Bozhou Zhang, Nan Song, Yuang Wang, Jiankang Deng, Xiatian Zhu, Li Zhang</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-05-08</div><div>2026-05-08</div><div><a href="http://arxiv.org/abs/2605.07195v1">2605.07195v1</a> / <a href="https://arxiv.org/pdf/2605.07195v1">PDF</a></div><div>cs.CV</div></td>
      <td style="width: 10%; vertical-align: top;">world model</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>当前的端到端自动驾驶规划器本质上是被动的：它们根据历史和当前的观测来预测未来的动作。我们认为，自动驾驶智能体应该在做出决定之前想象未来的场景，就像人类驾驶员在行动前会心理模拟“接下来会发生什么”一样。我们引入了 ForeSight，一个以基础世界模型为中心的规划框架，它将自动驾驶重新定义为预见性决策。ForeSight 没有将世界模型视为辅助组件，而是将未来场景的想象作为动作预测的主要驱动力。我们的方法分两个阶段运行：（1）通过预训练的世界模型生成合理的未来视觉世界，以及（2）根据这些想象的未来规划动作。这种从“我现在该做什么？”到“会发生什么，我该如何应对？”的范式转变，实现了真正的预见性规划而非被动式规划。通过将决策基于预期的情境而非仅仅当前的观测，ForeSight 更有效地应对动态、交互式场景。在 NAVSIM 和 nuScenes 上的大量实验表明，显式的未来想象显著优于之前的最先进替代方案，验证了我们这种预见性驱动的方法。</td>
      <td style="width: 20%; vertical-align: top;">当前自动驾驶规划器多为被动式，仅依据历史和当前观测做决策。本论文提出了 ForeSight 框架，通过引入基础世界模型来想象未来场景，进而在此基础上规划动作，将自动驾驶重塑为预见性决策。实验结果表明，这种预见性驱动的方法能够更有效地应对动态交互场景，并显著超越了现有最先进的替代方案。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>6. GSDrive: Reinforcing Driving Policies by Multi-mode Trajectory Probing with 3D Gaussian Splatting Environment</strong><br><span>Ziang Guo, Chen Min, Xuefeng Zhang, Yixiao Zhou, Zufeng Zhang, Dzmitry Tsetserukou</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-04-30</div><div>2026-05-01</div><div><a href="http://arxiv.org/abs/2604.28111v2">2604.28111v2</a> / <a href="https://arxiv.org/pdf/2604.28111v2">PDF</a></div><div>cs.RO</div></td>
      <td style="width: 10%; vertical-align: top;">RL</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>端到端（E2E）自动驾驶提供了一种有前景的方法，可将感知输入直接转化为驾驶动作。然而，高昂的标注成本和时序数据质量下降阻碍了其长期实际部署。尽管结合模仿学习（IL）和强化学习（RL）是改进策略的常见策略，但传统的RL训练依赖于延迟的、基于事件的奖励——策略仅从碰撞等灾难性结果中学习，导致过早收敛到次优行为。为了解决这些局限性，我们引入了GSDrive，这是一个利用3D高斯泼溅（3DGS）进行端到端驾驶策略改进中可微分、基于物理的奖励塑形的框架。我们的方法在3DGS模拟器中整合了一个基于流匹配的轨迹预测器，实现了多模态轨迹探测，其中候选轨迹被模拟以评估预期奖励。这通过将奖励函数建立在物理模拟的交互信号上，在IL和RL之间建立了双向知识交换，提供了即时密集反馈，而非稀疏的灾难性事件。在重建的nuScenes数据集上进行评估，我们的方法在闭环实验中超越了现有基于仿真的RL驾驶方法。代码可在 https://github.com/ZionGo6/GSDrive 获取。</td>
      <td style="width: 20%; vertical-align: top;">端到端自动驾驶面临高昂标注成本和传统强化学习中稀疏、延迟奖励导致策略次优的问题。GSDrive提出了一个框架，利用3D高斯泼溅（3DGS）在端到端驾驶策略改进中提供可微分、基于物理的奖励塑形，并通过在3DGS模拟器中嵌入流匹配的轨迹预测器进行多模态轨迹探测来评估潜在奖励。该方法在模仿学习和强化学习之间建立了双向知识交换，提供即时密集反馈，并在重建的nuScenes数据集上的闭环实验中超越了现有基于仿真的RL驾驶方法。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>7. ProDrive: Proactive Planning for Autonomous Driving via Ego-Environment Co-Evolution</strong><br><span>Chuyao Fu, Shengzhe Gan, Zhuoli Ouyang, Yuhan Rui, Xiaowei Chi, Sirui Han, Jiankun Wang, Hong Zhang</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-04-28</div><div>2026-04-28</div><div><a href="http://arxiv.org/abs/2604.25329v1">2604.25329v1</a> / <a href="https://arxiv.org/pdf/2604.25329v1">PDF</a></div><div>cs.RO</div></td>
      <td style="width: 10%; vertical-align: top;">world model</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>端到端自动驾驶规划器通常仅根据当前观测生成轨迹。然而，现实世界的驾驶高度动态，这种反应式规划无法预测未来的场景演变，常常导致短视决策和安全关键故障。我们提出了 ProDrive，一个基于世界模型的主动规划框架，它能够实现自动驾驶中的自我-环境协同演化。ProDrive 端到端地联合训练一个以查询为中心的轨迹规划器和一个鸟瞰图（BEV）世界模型：规划器生成多样化的候选轨迹和规划感知的自我令牌，而世界模型则根据这些信息预测未来的场景演变。通过将规划器特征注入世界模型并并行评估所有候选方案，ProDrive 保留了端到端梯度流，并允许对未来结果的评估直接影响规划。这种双向耦合使得主动规划超越了当前观测驱动的决策。在 NAVSIM v1 上的实验表明，ProDrive 在安全性和规划效率方面均优于强大的基线，而消融实验则验证了所提出的自我-环境耦合设计的有效性。</td>
      <td style="width: 20%; vertical-align: top;">传统自动驾驶规划器仅依赖当前观测，导致在动态环境中做出短视且可能不安全的决策。ProDrive 提出一个基于世界模型的主动规划框架，通过端到端地联合训练轨迹规划器和世界模型，实现自我-环境协同演化。该方法通过将规划器特征注入世界模型并评估未来结果来指导规划，实验证明其在安全性和规划效率上优于现有基线。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>8. Reasoning About Traversability: Language-Guided Off-Road 3D Trajectory Planning</strong><br><span>Byounggun Park, Soonmin Hwang</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-04-23</div><div>2026-04-23</div><div><a href="http://arxiv.org/abs/2604.21249v1">2604.21249v1</a> / <a href="https://arxiv.org/pdf/2604.21249v1">PDF</a></div><div>cs.RO</div></td>
      <td style="width: 10%; vertical-align: top;">VLM</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>尽管视觉-语言模型（VLM）能够为端到端自动驾驶（尤其是在非结构化环境中）提供高级语义推理能力，但现有的越野数据集存在语言标注与车辆动作和地形几何形状弱对齐的问题。为解决这种不对齐问题，我们提出了一种语言精炼框架，将标注重构为与动作对齐的对，使VLM能够直接从单张图像生成精炼的场景描述和3D未来轨迹。为了进一步鼓励地形感知规划，我们引入了一种偏好优化策略，该策略构建了几何感知硬负样本，并明确惩罚与局部高程剖面不一致的轨迹。此外，我们提出了越野专用指标来量化可通行性符合度和高程一致性，解决了传统公路评估的局限性。在ORAD-3D基准上的实验表明，我们的方法将平均轨迹误差从1.01米降低到0.97米，将可通行性符合度从0.621提高到0.644，并将高程不一致性从0.428降低到0.322，这突出了动作对齐监督和地形感知优化对于鲁棒越野驾驶的有效性。</td>
      <td style="width: 20%; vertical-align: top;">针对越野自动驾驶中语言标注与车辆动作和地形几何结构不匹配的问题，本文提出了一种语言精炼框架，将标注重构为与动作对齐的对，并引入偏好优化策略，通过几何感知硬负样本来鼓励地形感知规划。该方法使视觉-语言模型能够直接从图像生成地形感知的3D轨迹。在ORAD-3D基准上的实验表明，本文方法显著降低了轨迹误差，提高了可通行性符合度并减少了高程不一致性，验证了其在鲁棒越野驾驶中的有效性。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>9. SpanVLA: Efficient Action Bridging and Learning from Negative-Recovery Samples for Vision-Language-Action Model</strong><br><span>Zewei Zhou, Ruining Yang, Xuewei, Qi, Yiluan Guo, Sherry X. Chen, Tao Feng, Kateryna Pistunova, Yishan Shen, Lili Su, Jiaqi Ma</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-04-21</div><div>2026-04-21</div><div><a href="http://arxiv.org/abs/2604.19710v1">2604.19710v1</a> / <a href="https://arxiv.org/pdf/2604.19710v1">PDF</a></div><div>cs.CV</div></td>
      <td style="width: 10%; vertical-align: top;">VLM</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>视觉-语言-动作 (VLA) 模型提供了一种有前途的自动驾驶范式，可以利用世界知识和推理能力，尤其是在长尾场景中。然而，现有的 VLA 模型在使用自回归生成框架进行动作生成时，经常面临高延迟问题，并且表现出有限的鲁棒性。在本文中，我们提出了 SpanVLA，一个新颖的端到端自动驾驶框架，它整合了自回归推理和一个流匹配动作专家。首先，SpanVLA 引入了一种高效的桥接机制，利用视觉语言模型 (VLM) 的视觉和推理指导，通过以历史轨迹初始化为条件的流匹配策略来高效规划未来轨迹，这显著减少了推理时间。其次，为了进一步提高 SpanVLA 模型的性能和鲁棒性，我们提出了一种基于 GRPO 的后训练方法，使 VLA 模型不仅能从积极的驾驶样本中学习，还能学习如何避免典型的负面行为并学习恢复行为。我们进一步介绍了 mReasoning，一个关注复杂、需要推理的场景以及负面-恢复样本的全新真实世界驾驶推理数据集。在 NAVSIM (v1 和 v2) 上的大量实验证明了 SpanVLA 模型的竞争性性能。此外，在不同场景下的定性结果突出了我们模型的规划性能和鲁棒性。</td>
      <td style="width: 20%; vertical-align: top;">本文针对现有视觉-语言-动作 (VLA) 模型在自动驾驶中动作生成高延迟和鲁棒性不足的问题，提出了 SpanVLA 框架。该框架通过一个高效桥接机制将 VLM 的推理能力与流匹配动作专家结合，显著降低了轨迹规划的推理时间；同时，引入基于 GRPO 的后训练方法，使模型能从正面及负面恢复样本中学习，并提出了 mReasoning 数据集以强化复杂场景推理。实验结果表明 SpanVLA 在规划性能和鲁棒性上具有强大的竞争力。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>10. From Particles to Perils: SVGD-Based Hazardous Scenario Generation for Autonomous Driving Systems Testing</strong><br><span>Linfeng Liang, Xiao Cheng, Tsong Yueh Chen, Xi Zheng</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-04-20</div><div>2026-04-20</div><div><a href="http://arxiv.org/abs/2604.18918v1">2604.18918v1</a> / <a href="https://arxiv.org/pdf/2604.18918v1">PDF</a></div><div>cs.SE, cs.LG</div></td>
      <td style="width: 10%; vertical-align: top;">RL</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>自动驾驶系统（ADS）的基于仿真的测试必须在密集、异构的交通中发现真实且多样化的故障。然而，现有的基于搜索的种子生成方法（例如遗传算法）在高维空间中表现不佳，常常收敛到有限的模式并遗漏许多故障场景。我们提出了 PtoP，一个结合自适应随机种子生成和斯坦变分梯度下降（SVGD）的框架，以生成多样化、能诱发故障的初始条件。SVGD 平衡了向高风险区域的吸引力和粒子之间的排斥力，从而产生了寻求风险但又在多个故障模式中分布良好的种子。PtoP 是即插即用的，通过提供有原则的种子来增强现有的在线测试方法（例如基于强化学习的测试器）。在 CARLA 中对两个工业级 ADS（Apollo、Autoware）和一个原生端到端系统进行的评估表明，PtoP 在安全违规率（高达 27.68%）、场景多样性（9.6%）和地图覆盖率（16.78%）方面均优于基线方法。</td>
      <td style="width: 20%; vertical-align: top;">自动驾驶系统测试中，现有搜索方法在高维空间难以有效生成多样化故障场景。本文提出 PtoP 框架，结合自适应随机种子生成与斯坦变分梯度下降（SVGD），以产生多样化、能诱发故障的初始条件。实验证明，PtoP 能显著提高安全违规率、场景多样性和地图覆盖率，有效增强现有在线测试方法。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>11. Asset Harvester: Extracting 3D Assets from Autonomous Driving Logs for Simulation</strong><br><span>Tianshi Cao, Jiawei Ren, Yuxuan Zhang, Jaewoo Seo, Jiahui Huang, Shikhar Solanki, Haotian Zhang, Mingfei Guo, Haithem Turki, Muxingzi Li, Yue Zhu, Sipeng Zhang, Zan Gojcic, Sanja Fidler, Kangxue Yin</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-04-20</div><div>2026-04-20</div><div><a href="http://arxiv.org/abs/2604.18468v1">2604.18468v1</a> / <a href="https://arxiv.org/pdf/2604.18468v1">PDF</a></div><div>cs.CV, cs.AI, cs.GR, cs.LG</div></td>
      <td style="width: 10%; vertical-align: top;">distillation</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>闭环仿真作为自动驾驶车辆 (AV) 开发的核心组成部分，使得在实际部署前进行可扩展的测试、训练和安全验证成为可能。神经场景重建能将驾驶日志转换为用于仿真的交互式 3D 环境，但它无法生成代理操纵和大规模视角新视图合成所需的完整 3D 对象资产。为解决这一挑战，我们提出了 Asset Harvester，这是一个图像到 3D 模型和端到端管线，能将来自真实驾驶日志的稀疏、野外对象观测转换为完整的、可用于仿真的资产。我们没有仅仅依赖单一模型组件，而是为真实世界的 AV 数据开发了一个系统级设计，该设计结合了以对象为中心的大规模训练元组的策划、跨异构传感器的几何感知预处理，以及一个稳健的训练配方，将稀疏视图条件下的多视图生成与 3D 高斯提升相结合。在此系统内，SparseViewDiT 经过专门设计，用于解决有限角度视图和其他真实世界数据挑战。结合混合数据策划、增强和自蒸馏，该系统能够将稀疏的 AV 对象观测可扩展地转换为可重用的 3D 资产。</td>
      <td style="width: 20%; vertical-align: top;">自动驾驶车辆的闭环仿真急需完整的 3D 对象资产，但现有神经场景重建无法提供。本文提出了 Asset Harvester，一个端到端的图像到 3D 管线，能将驾驶日志中稀疏的野外对象观测转换为完整的、可用于仿真的 3D 资产。该系统通过大规模数据整理、几何感知预处理和结合稀疏视图条件多视图生成与 3D 高斯提升的稳健训练方法，实现了可扩展的 3D 资产提取。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>12. OneDrive: Unified Multi-Paradigm Driving with Vision-Language-Action Models</strong><br><span>Yiwei Zhang, Xuesong Chen, Jin Gao, Hanshi Wang, Fudong Ge, Weiming Hu, Shaoshuai Shi, Zhipeng Zhang</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-04-20</div><div>2026-04-20</div><div><a href="http://arxiv.org/abs/2604.17915v1">2604.17915v1</a> / <a href="https://arxiv.org/pdf/2604.17915v1">PDF</a></div><div>cs.CV</div></td>
      <td style="width: 10%; vertical-align: top;">VLM</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>视觉语言模型（VLM）在自回归文本生成方面表现出色，然而，端到端自动驾驶需要多任务学习，包括结构化输出和异构解码行为，例如自回归语言生成、并行目标检测和轨迹回归。为了适应这些差异，现有系统通常引入单独或级联的解码器，导致架构碎片化和骨干网络重用受限。在这项工作中，我们提出了一个基于预训练 VLM 的统一自动驾驶框架，其中异构解码行为在单个 Transformer 解码器中得到协调。我们证明了预训练 VLM 的注意力机制在纯语言建模之外表现出强大的可迁移性。通过在单个因果解码器中组织视觉和结构化查询令牌，结构化查询可以通过原始注意力机制自然地依赖视觉上下文。文本和结构化输出共享一个共同的注意力骨干网络，从而实现异构任务之间的稳定联合优化。轨迹规划通过引入结构化轨迹查询在同一因果 LLM 解码器中实现。这种统一的公式使得规划能够与图像和感知令牌共享预训练的注意力骨干网络。在端到端自动驾驶基准测试中进行的广泛实验证明了最先进的性能，包括 nuScenes 开放循环评估中的 0.28 L2 和 0.18 碰撞率，以及 NAVSIM 闭环评估中的竞争性结果（86.8 PDMS）。完整模型保留了多模态生成能力，而高效推理模式将延迟降低了约 40%。代码和模型可在 https://github.com/Z1zyw/OneDrive 获取。</td>
      <td style="width: 20%; vertical-align: top;">该论文提出了一个名为 OneDrive 的统一自动驾驶框架，它基于预训练的视觉语言模型（VLM）。该框架通过在一个 Transformer 解码器中整合不同的解码行为，解决了现有系统因使用独立解码器而导致的架构碎片化问题。OneDrive 证明了预训练 VLM 的注意力机制在自动驾驶任务中具有很强的迁移能力，并在 nuScenes 和 NAVSIM 等端到端自动驾驶基准测试中取得了最先进的性能。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>13. Infrastructure-Centric World Models: Bridging Temporal Depth and Spatial Breadth for Roadside Perception</strong><br><span>Siyuan Meng, Chengbo Ai</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-04-19</div><div>2026-04-19</div><div><a href="http://arxiv.org/abs/2604.17651v1">2604.17651v1</a> / <a href="https://arxiv.org/pdf/2604.17651v1">PDF</a></div><div>cs.CV, cs.RO</div></td>
      <td style="width: 10%; vertical-align: top;">world model</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>世界模型，即模拟环境演变方式的生成式AI系统，正在彻底改变自动驾驶领域，然而所有现有方法都采用以自我车辆为中心的视角，而忽略了基础设施视角。我们认为，以基础设施为中心的世界模型提供了一种根本上互补的能力：路侧系统独有的鸟瞰、多传感器、持久的视角。我们论点核心是时空互补性：固定的路侧传感器擅长时间深度，能够积累包括罕见安全关键事件在内的长期行为分布，而车载传感器擅长空间广度，可以在大型道路网络中采样多样化的场景。本文提出了一个分为三个阶段的以基础设施为中心的世界模型（I-WM）愿景：(I) 具有质量感知不确定性传播的生成式场景理解，(II) 具有多智能体反事实推理的物理感知预测动力学，以及 (III) 通过潜在空间对齐实现V2X通信的协作世界模型。我们提出了一种双层架构，将无标注感知作为多模态数据引擎，为端到端生成式世界模型提供数据，并采用从激光雷达到4D雷达、信号相位数据再到事件相机的分阶段传感器策略。我们建立了驾驶世界模型范式的分类体系，将I-WM置于LeCun的JEPA、李飞飞的空间智能和VLA架构的背景下进行定位，并引入基础设施VLA（I-VLA）作为路侧感知、语言指令和交通控制行动的新型统一体。我们的愿景建立在现有多激光雷达管道之上，并确定了每个阶段的开源基础，为实现能够理解和预测交通的基础设施提供了一条途径。</td>
      <td style="width: 20%; vertical-align: top;">当前自动驾驶世界模型主要以车载视角为主，忽略了基础设施视角。本文提出了一种以基础设施为中心的世界模型（I-WM）愿景，利用路侧系统的鸟瞰、多传感器优势，实现时空互补的生成式场景理解和预测动力学。通过双层架构和分阶段传感器策略，该研究旨在构建能够理解并预测交通的基础设施，并引入基础设施VLA（I-VLA）统一路侧感知、语言指令和交通控制。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>14. Beyond Conservative Automated Driving in Multi-Agent Scenarios via Coupled Model Predictive Control and Deep Reinforcement Learning</strong><br><span>Saeed Rahmani, Gözde Körpe, Zhenlin, Xu, Bruno Brito, Simeon Craig Calvert, Bart van Arem</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-04-15</div><div>2026-04-15</div><div><a href="http://arxiv.org/abs/2604.13891v1">2604.13891v1</a> / <a href="https://arxiv.org/pdf/2604.13891v1">PDF</a></div><div>cs.RO, cs.AI, eess.SY</div></td>
      <td style="width: 10%; vertical-align: top;">RL</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>无信号灯交叉路口的自动驾驶具有挑战性，原因在于复杂的车辆间交互以及需要在安全性和效率之间取得平衡。模型预测控制 (MPC) 通过优化提供结构化的约束处理，但它依赖于手工设计的规则，这些规则通常会产生过于保守的行为。深度强化学习 (RL) 从经验中学习适应性行为，但通常在安全保障和对未见环境的泛化方面遇到困难。在本研究中，我们提出了一种集成的 MPC-RL 框架，以提高多智能体场景中的导航性能。实验表明，MPC-RL 在三种交通密度水平下均优于独立的 MPC 和端到端 RL。总体而言，与纯 MPC 相比，MPC-RL 将碰撞率降低了 21%，成功率提高了 6.5%。我们进一步评估了在不重新训练的情况下对高速公路合并场景进行零样本迁移。基于 MPC 的方法都比端到端 PPO 具有更好的迁移能力，这突出了 MPC 主干在跨场景鲁棒性中的作用。该框架在训练期间还显示出比端到端 RL 更快的损失稳定速度，这表明学习负担有所减轻。这些结果表明，该集成方法可以在多智能体交叉路口场景中改善安全性能和效率之间的平衡，同时 MPC 组件为跨驾驶环境的泛化提供了坚实的基础。实施代码已开源。</td>
      <td style="width: 20%; vertical-align: top;">本研究旨在解决无信号灯交叉路口自动驾驶中安全性与效率难以平衡的问题，指出传统 MPC 过于保守而纯 RL 缺乏安全保障和泛化能力。作者提出了一种集成的 MPC-RL 框架，以结合两者的优势。实验结果表明，该框架在多智能体场景下显著优于独立 MPC 和端到端 RL，不仅降低了碰撞率并提高了成功率，还展示了更好的跨场景泛化能力和更快的训练收敛速度。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>15. Learning Vision-Language-Action World Models for Autonomous Driving</strong><br><span>Guoqing Wang, Pin Tang, Xiangxuan Ren, Guodongfang Zhao, Bailan Feng, Chao Ma</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-04-10</div><div>2026-04-10</div><div><a href="http://arxiv.org/abs/2604.09059v1">2604.09059v1</a> / <a href="https://arxiv.org/pdf/2604.09059v1">PDF</a></div><div>cs.CV, cs.AI</div></td>
      <td style="width: 10%; vertical-align: top;">world model, RL</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>视觉-语言-动作 (VLA) 模型最近在端到端自动驾驶领域取得了显著进展，它将感知、推理和控制集成到统一的多模态框架中。然而，它们通常缺乏对时间动态和全局世界一致性的明确建模，这限制了它们的预见性和安全性。相比之下，世界模型可以模拟合理的未来场景，但通常难以对其生成的想象未来进行推理或评估。在这项工作中，我们提出了 VLA-World，一个简单而有效的 VLA 世界模型，它将预测性想象与反思性推理相结合，以提高驾驶预见性。VLA-World 首先利用动作衍生的可行轨迹来指导下一帧图像的生成，捕获描述周围环境如何演变的丰富的空间和时间线索。然后，模型对这个自我生成的未来想象帧进行推理，以完善预测轨迹，从而实现更高的性能和更好的可解释性。为了支持这一流程，我们整理了 nuScenes-GR-20K，一个源自 nuScenes 的生成式推理数据集，并采用了包括预训练、监督微调和强化学习在内的三阶段训练策略。大量实验表明，VLA-World 在规划和未来生成基准测试中，始终超越了最先进的 VLA 和世界模型基线。项目页面：https://vlaworld.github.io</td>
      <td style="width: 20%; vertical-align: top;">现有端到端自动驾驶VLA模型缺乏时间动态和全局一致性建模，限制了其预见性，而世界模型虽能模拟未来但难以推理。本文提出VLA-World，一个结合预测性想象和反思性推理的VLA世界模型，它利用动作轨迹指导未来场景生成，再对生成结果进行推理以优化预测轨迹。该模型显著提升了自动驾驶的预见性、性能和可解释性，并在规划和未来生成任务上超越了当前先进基线。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>16. LMGenDrive: Bridging Multimodal Understanding and Generative World Modeling for End-to-End Driving</strong><br><span>Hao Shao, Letian Wang, Yang Zhou, Yuxuan Hu, Zhuofan Zong, Steven L. Waslander, Wei Zhan, Hongsheng Li</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-04-09</div><div>2026-04-09</div><div><a href="http://arxiv.org/abs/2604.08719v1">2604.08719v1</a> / <a href="https://arxiv.org/pdf/2604.08719v1">PDF</a></div><div>cs.CV, cs.AI, cs.RO</div></td>
      <td style="width: 10%; vertical-align: top;">VLM, world model</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>近年来，自动驾驶取得了显著进展，但泛化到长尾和开放世界场景仍然是大规模部署的主要瓶颈。为应对这一挑战，一些研究利用大型语言模型（LLMs）和视觉语言模型（VLMs）进行视觉-语言理解和推理，使车辆在生成动作时能够解释罕见和安全关键的情境。另一些研究则探索生成式世界模型，以捕捉驾驶场景的时空演变，使智能体能够在行动前设想可能的未来。受人类智能统一理解和想象的启发，我们探索了一种用于自动驾驶的统一模型。我们提出了LMGenDrive，这是第一个将基于LLM的多模态理解与生成式世界模型相结合，实现端到端闭环驾驶的框架。鉴于多视角摄像头输入和自然语言指令，LMGenDrive能够生成未来的驾驶视频和控制信号。这种设计提供了互补的优势：视频预测改善了时空场景建模，而LLM则从大规模预训练中贡献了强大的语义先验和指令基础。我们进一步提出了一种渐进式三阶段训练策略，从视觉预训练到多步长时程驾驶，以提高稳定性和性能。LMGenDrive支持低延迟在线规划和自回归离线视频生成。实验表明，它在具有挑战性的闭环基准测试中显著优于现有方法，在指令遵循、时空理解以及对罕见场景的鲁棒性方面均有明显提升。这些结果表明，统一多模态理解和生成是实现更具泛化性和鲁棒性的具身决策系统的一个有前景的方向。</td>
      <td style="width: 20%; vertical-align: top;">本文旨在解决自动驾驶在长尾和开放世界场景中泛化能力不足的问题，通过统一理解与想象来提升性能。作者提出了LMGenDrive框架，它首次将基于LLM的多模态理解与生成式世界模型相结合，用于端到端闭环驾驶，能够同时生成未来驾驶视频和控制信号。实验结果表明，LMGenDrive在指令遵循、时空理解和罕见场景的鲁棒性方面显著优于现有方法，为实现更具泛化性和鲁棒性的自动驾驶系统提供了新方向。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>17. Fuzzy Encoding-Decoding to Improve Spiking Q-Learning Performance in Autonomous Driving</strong><br><span>Aref Ghoreishee, Abhishek Mishra, Lifeng Zhou, John Walsh, Anup Das, Nagarajan Kandasamy</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-04-06</div><div>2026-04-06</div><div><a href="http://arxiv.org/abs/2604.16436v1">2604.16436v1</a> / <a href="https://arxiv.org/pdf/2604.16436v1">PDF</a></div><div>cs.NE, cs.LG</div></td>
      <td style="width: 10%; vertical-align: top;">RL</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>本文开发了一种端到端的模糊编码-解码架构，用于增强自动驾驶中基于视觉的多模态深度脉冲Q网络。该方法解决了脉冲强化学习的两个核心局限性：一是密集视觉输入转换为稀疏脉冲序列导致的信息损失，二是基于脉冲的价值函数表示能力有限，这通常导致Q值估计的区分度较弱。编码器引入了可训练的模糊隶属函数来生成富有表现力的、基于种群的脉冲表示，解码器则使用轻量级神经解码器从脉冲输出中重建连续的Q值。在HighwayEnv基准上的实验表明，所提出的架构显著提高了决策准确性，并缩小了脉冲与非脉冲多模态Q网络之间的性能差距。结果突出了该框架在利用脉冲神经网络实现高效实时自动驾驶方面的潜力。</td>
      <td style="width: 20%; vertical-align: top;">这篇论文解决了脉冲强化学习在自动驾驶中面临的信息损失和Q值区分度不足的问题。研究人员提出了一种端到端的模糊编码-解码架构，通过模糊隶属函数生成丰富的脉冲表示，并利用神经解码器重建连续Q值。实验结果表明，该方法显著提升了决策准确性，缩小了脉冲与非脉冲Q网络间的性能差距，展现了其在高效实时自动驾驶中的潜力。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>18. HAD: Combining Hierarchical Diffusion with Metric-Decoupled RL for End-to-End Driving</strong><br><span>Wenhao Yao, Xinglong Sun, Zhenxin Li, Shiyi Lan, Zi Wang, Jose M. Alvarez, Zuxuan Wu</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-04-04</div><div>2026-04-04</div><div><a href="http://arxiv.org/abs/2604.03581v1">2604.03581v1</a> / <a href="https://arxiv.org/pdf/2604.03581v1">PDF</a></div><div>cs.RO, cs.CV</div></td>
      <td style="width: 10%; vertical-align: top;">RL</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>端到端规划已成为自动驾驶的主导范式，其中最近的模型通常采用评分-选择框架从大量候选轨迹中进行选择，而基于扩散的解码显示出强大的前景。然而，直接从整个候选空间中选择仍然难以优化，并且扩散中使用的 Gaussian 扰动常常引入不切实际的轨迹，从而使去噪过程复杂化。此外，为了训练这些模型，强化学习 (RL) 显示出前景，但现有的端到端 RL 方法通常依赖于没有结构化信号的单一耦合奖励，从而限制了优化效率。为了解决这些挑战，我们提出了 HAD，一个具有分层扩散策略的端到端规划框架，它将规划分解为从粗到精的过程。为了改进轨迹生成，我们引入了结构保持轨迹扩展，它在保持运动学结构的同时生成真实的候选轨迹。为了策略学习，我们开发了度量解耦策略优化 (MDPO)，以实现跨多个驾驶目标的结构化 RL 优化。大量实验表明，HAD 在 NAVSIM 和 HUGSIM 上均实现了新的最先进性能，以巨大的优势超越了现有技术：NAVSIM 上提高了 +2.3 EPDMS，HUGSIM 上提高了 +4.9 路线完成度。</td>
      <td style="width: 20%; vertical-align: top;">本研究旨在解决自动驾驶端到端规划中轨迹选择优化困难、扩散模型生成非真实轨迹以及强化学习奖励耦合导致的优化效率低下等问题。为此，论文提出了 HAD 框架，结合分层扩散策略以粗到精的方式进行规划，并利用结构保持轨迹扩展生成真实轨迹，同时采用度量解耦策略优化实现多目标强化学习。实验证明，HAD 在 NAVSIM 和 HUGSIM 数据集上均达到了最先进的性能，显著优于现有方法。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>19. ExploreVLA: Dense World Modeling and Exploration for End-to-End Autonomous Driving</strong><br><span>Zihao Sheng, Xin Ye, Jingru Luo, Sikai Chen, Liu Ren</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-04-03</div><div>2026-04-03</div><div><a href="http://arxiv.org/abs/2604.02714v1">2604.02714v1</a> / <a href="https://arxiv.org/pdf/2604.02714v1">PDF</a></div><div>cs.CV</div></td>
      <td style="width: 10%; vertical-align: top;">world model, RL</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>基于视觉-语言-动作（VLA）架构的端到端自动驾驶模型通过在专家演示上进行行为克隆学习驾驶策略，已显示出有希望的结果。然而，模仿学习固有地将模型限制在复制观察到的行为，而无法探索多样化的驾驶策略，使其在新颖或分布外场景中表现脆弱。强化学习（RL）通过实现超越专家分布的策略探索，提供了一种自然的补救方法。然而，VLA模型通常在离线数据集上训练，缺乏直接可观察的状态转换，因此需要一个学习到的世界模型来预测动作后果。在这项工作中，我们提出了一个统一的理解-生成框架，该框架利用世界建模同时实现有意义的探索并提供密集监督。具体来说，我们将轨迹预测与未来RGB和深度图像生成相结合，作为密集世界建模目标，要求模型学习细粒度的视觉和几何表示，从而极大地丰富规划主干。除了作为监督信号外，世界模型还充当策略探索的内在奖励来源：其图像预测不确定性自然地衡量轨迹相对于训练分布的新颖性，其中高不确定性表示分布外场景，如果安全，则代表有价值的学习机会。我们将这种探索信号整合到一个安全门控奖励中，并通过群组相对策略优化（GRPO）来优化策略。在NAVSIM和nuScenes基准测试上的实验证明了我们方法的有效性，在NAVSIM上实现了93.7的PDMS分数和88.8的EPDMS分数，达到了最先进水平。代码和演示将在 https://zihaosheng.github.io/ExploreVLA/ 公开提供。</td>
      <td style="width: 20%; vertical-align: top;">针对端到端VLA自动驾驶模型在陌生场景中探索不足的问题，本文提出了ExploreVLA框架。该框架利用密集世界模型预测未来的RGB和深度图像，从而提供丰富的视觉几何表示进行规划，并以预测不确定性作为内在奖励来指导安全探索。实验表明，ExploreVLA在NAVSIM和nuScenes基准测试上实现了最先进的性能。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>20. $AutoDrive\text{-}P^3$: Unified Chain of Perception-Prediction-Planning Thought via Reinforcement Fine-Tuning</strong><br><span>Yuqi Ye, Zijian Zhang, Junhong Lin, Shangkun Sun, Changhao Peng, Wei Gao</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-03-30</div><div>2026-03-30</div><div><a href="http://arxiv.org/abs/2603.28116v1">2603.28116v1</a> / <a href="https://arxiv.org/pdf/2603.28116v1">PDF</a></div><div>cs.RO, cs.CV</div></td>
      <td style="width: 10%; vertical-align: top;">VLM, RL</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>视觉语言模型（VLM）因其在处理长尾场景方面的卓越表现，正越来越多地被采用于端到端自动驾驶系统。然而，当前基于VLM的方法存在两个主要局限性：1）一些VLM直接输出规划结果，没有经过思维链（CoT）推理，绕过了关键的感知和预测阶段，这产生了显著的领域差距并损害了决策能力；2）其他VLM可以为感知、预测和规划任务生成输出，但采用的是碎片化的决策方法，这些模块独立运行，导致协同作用严重缺乏，从而削弱了真正的规划性能。为了解决这些局限性，我们提出了${AutoDrive\text{-}P^3}$，一个通过结构化推理无缝整合\textbf{感知}、\textbf{预测}和\textbf{规划}的新颖框架。我们引入了${P^3\text{-}CoT}$数据集以促进连贯推理，并提出了${P^3\text{-}GRPO}$，一种分层强化学习算法，为所有三个任务提供渐进式监督。具体而言，${AutoDrive\text{-}P^3}$逐步生成感知、预测和规划的CoT推理和答案，其中感知为后续的预测和规划提供基本信息，而感知和预测共同为最终的规划决策做出贡献，从而实现更安全、更可解释的自动驾驶。此外，为了平衡推理效率和性能，我们引入了双重思维模式：详细思维和快速思维。在开环（nuScenes）和闭环（NAVSIMv1/v2）基准上进行的广泛实验表明，我们的方法在规划任务中取得了最先进的性能。代码可在https://github.com/haha-yuki-haha/AutoDrive-P3获取。</td>
      <td style="width: 20%; vertical-align: top;">当前基于视觉语言模型的自动驾驶系统存在思维链缺失或感知-预测-规划模块协同不足的问题。为解决此，${AutoDrive\text{-}P^3}$框架通过结构化推理无缝整合感知、预测和规划，并引入${P^3\text{-}CoT}$数据集和分层强化学习算法${P^3\text{-}GRPO}$以实现协同决策。该方法通过逐步生成思维链推理，实现了更安全、可解释的自动驾驶，并在多个基准测试中展现出最先进的规划性能。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>21. Collision-Aware Vision-Language Learning for End-to-End Driving with Multimodal Infraction Datasets</strong><br><span>Alex Koran, Dimitrios Sinodinos, Hadi Hojjati, Takuya Nanri, Fangge Chen, Narges Armanfard</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-03-26</div><div>2026-03-26</div><div><a href="http://arxiv.org/abs/2603.25946v1">2603.25946v1</a> / <a href="https://arxiv.org/pdf/2603.25946v1">PDF</a></div><div>cs.CV, cs.AI, cs.LG</div></td>
      <td style="width: 10%; vertical-align: top;">VLM</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>高违规率仍然是端到端（E2E）自动驾驶的主要瓶颈，这在CARLA排行榜上的低驾驶分数中得到了体现。尽管与碰撞相关的违规是闭环评估中的主要故障模式，但碰撞感知表征学习受到的关注有限。为了解决这一空白，我们首先开发了一个视频-语言增强异常检测器（VLAAD），它利用多实例学习（MIL）公式来获取稳定、时间局部化的碰撞信号，用于主动预测。为了将这些能力转化到闭环模拟中，我们必须克服现有模拟器数据集的局限性，这些数据集缺乏多模态性，并且经常局限于简单的交叉路口场景。因此，我们引入了CARLA-Collide，这是一个大规模多模态数据集，用于捕获高度多样化路网中的真实碰撞事件。在这些多样化的模拟器数据上进行训练后，VLAAD可作为一个碰撞感知插件模块，无缝集成到现有的E2E驾驶模型中。通过将我们的模块集成到预训练的TransFuser++代理中，我们证明了在最小微调的情况下，驾驶分数相对提高了14.12%。除了闭环评估，我们还使用真实世界的驾驶数据在开环设置中进一步评估了VLAAD的泛化能力。为了支持这项分析，我们引入了Real-Collide，这是一个多模态数据集，包含多样化的行车记录仪视频，并配有语义丰富的碰撞检测和预测注释。在此基准上，尽管VLAAD仅包含0.6亿参数，但它超越了一个多亿参数的视觉-语言模型，在AUC方面实现了23.3%的改进。</td>
      <td style="width: 20%; vertical-align: top;">端到端自动驾驶面临高违规率（尤其是碰撞）瓶颈，而碰撞感知学习不足。本文提出VLAAD（视频-语言增强异常检测器），利用多实例学习实现主动碰撞预测，并构建了CARLA-Collide和Real-Collide两个多模态数据集。VLAAD作为一个可插拔模块，能显著提升现有E2E驾驶模型的驾驶分数（相对提高14.12%），并在真实世界数据上展现出优异的泛化能力，超越了参数量更大的视觉-语言模型。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>22. COIN: Collaborative Interaction-Aware Multi-Agent Reinforcement Learning for Self-Driving Systems</strong><br><span>Yifeng Zhang, Jieming Chen, Tingguang Zhou, Tanishq Duhan, Jianghong Dong, Yuhong Cao, Guillaume Sartoretti</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-03-26</div><div>2026-03-26</div><div><a href="http://arxiv.org/abs/2603.24931v1">2603.24931v1</a> / <a href="https://arxiv.org/pdf/2603.24931v1">PDF</a></div><div>cs.RO</div></td>
      <td style="width: 10%; vertical-align: top;">RL</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>多智能体自动驾驶（MASD）系统为协调自动驾驶车辆提供了一种有效的解决方案，旨在未来智能交通系统中减少拥堵，并提高安全性和运营效率。多智能体强化学习（MARL）已成为开发先进的端到端MASD系统的一种有前途的方法。然而，在具有复杂智能体交互的密集场景中，实现动态MASD系统中的高效安全协作仍然是一个重大挑战。为了解决这一挑战，我们提出了一种新颖的协作式（CO-）交互感知（-IN）MARL框架，命名为COIN。具体来说，我们开发了一种新的反事实个体-全局双延迟深度确定性策略梯度（CIG-TD3）算法，该算法以“集中式训练、分布式执行”（CTDE）方式精心设计，旨在共同优化智能体的个体目标（导航）和全局目标（协作）。我们进一步引入了一种双层交互感知集中式评论家架构，该架构捕获了局部成对交互和全局系统级依赖关系，从而实现了更准确的全局价值估计和改进的信用分配，以促进协作策略学习。我们在密集的城市交通环境中进行了广泛的仿真实验，结果表明，COIN在各种系统规模下，在安全性和效率方面始终优于其他先进的基线方法。这些结果突显了其在复杂动态MASD场景中的优越性，并通过真实世界机器人演示得到了进一步验证。补充视频可在 https://marmotlab.github.io/COIN/ 查看。</td>
      <td style="width: 20%; vertical-align: top;">针对多智能体自动驾驶系统在复杂密集场景中实现高效安全协作的挑战，本文提出了COIN框架。该框架引入了CIG-TD3算法来同时优化智能体的个体和全局目标，并设计了双层交互感知集中式评论家架构以捕捉多层次交互。实验结果表明，COIN在安全性和效率方面均优于现有方法，验证了其在复杂MASD场景中的有效性。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>23. Latent-WAM: Latent World Action Modeling for End-to-End Autonomous Driving</strong><br><span>Linbo Wang, Yupeng Zheng, Qiang Chen, Shiwei Li, Yichen Zhang, Zebin Xing, Qichao Zhang, Xiang Li, Deheng Qian, Pengxuan Yang, Yihang Dong, Ce Hao, Xiaoqing Ye, Junyu han, Yifeng Pan, Dongbin Zhao</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-03-25</div><div>2026-03-25</div><div><a href="http://arxiv.org/abs/2603.24581v1">2603.24581v1</a> / <a href="https://arxiv.org/pdf/2603.24581v1">PDF</a></div><div>cs.CV, cs.RO</div></td>
      <td style="width: 10%; vertical-align: top;">world model</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>我们引入了Latent-WAM，这是一种高效的端到端自动驾驶框架，它通过空间感知和动态信息丰富的潜在世界表示实现强大的轨迹规划。现有的基于世界模型的规划器存在表示压缩不足、空间理解有限以及时间动态利用不足的问题，导致在受限的数据和计算预算下规划效果不佳。Latent-WAM通过两个核心模块解决了这些局限性：一个空间感知压缩世界编码器（SCWE），它从基础模型中提取几何知识，并通过可学习查询将多视图图像压缩为紧凑的场景令牌；以及一个动态潜在世界模型（DLWM），它采用因果Transformer，根据历史视觉和运动表示自回归地预测未来世界状态。在NAVSIM v2和HUGSIM上进行的大量实验表明，该方法取得了新的最先进结果：在NAVSIM v2上达到89.3 EPDMS，在HUGSIM上达到28.9 HD-Score，以显著更少的训练数据和紧凑的104M参数模型，超越了之前最佳的无感知方法3.2 EPDMS。</td>
      <td style="width: 20%; vertical-align: top;">本文介绍了Latent-WAM，一个用于端到端自动驾驶的框架，旨在解决现有世界模型在表示压缩、空间理解和时间动态方面的不足。它通过空间感知压缩世界编码器（SCWE）和动态潜在世界模型（DLWM）实现高效的轨迹规划。该方法在NAVSIM v2和HUGSIM上取得了最先进的成果，验证了其在数据和计算效率上的优越性。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>24. LongTail Driving Scenarios with Reasoning Traces: The KITScenes LongTail Dataset</strong><br><span>Royden Wagner, Omer Sahin Tas, Jaime Villa, Felix Hauser, Yinzhe Shen, Marlon Steiner, Dominik Strutz, Carlos Fernandez, Christian Kinzig, Guillermo S. Guitierrez-Cabello, Hendrik Königshof, Fabian Immel, Richard Schwarzkopf, Nils Alexander Rack, Kevin Rösch, Kaiwen Wang, Jan-Hendrik Pauls, Martin Lauer, Igor Gilitschenski, Holger Caesar, Christoph Stiller</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-03-24</div><div>2026-04-06</div><div><a href="http://arxiv.org/abs/2603.23607v2">2603.23607v2</a> / <a href="https://arxiv.org/pdf/2603.23607v2">PDF</a></div><div>cs.CV, cs.RO</div></td>
      <td style="width: 10%; vertical-align: top;">VLM</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>在自动驾驶等现实世界领域中，对罕见场景的泛化仍然是一个基本挑战。为了解决这个问题，我们引入了一个新的数据集，专为端到端驾驶设计，侧重于长尾驾驶事件。我们提供多视角视频数据、轨迹、高级指令和详细的推理轨迹，以促进上下文学习和少样本泛化。这个为多模态模型（如VLM和VLA）提供的基准测试，通过评估指令遵循和模型输出之间的语义连贯性，超越了安全和舒适性指标。英文、西班牙文和中文的多语言推理轨迹来自具有不同文化背景的领域专家。因此，我们的数据集是研究不同形式的推理如何影响驾驶能力的独特资源。我们的数据集可在：https://hf.co/datasets/kit-mrt/kitscenes-longtail 获取。</td>
      <td style="width: 20%; vertical-align: top;">自动驾驶在罕见场景的泛化能力上存在挑战。为解决此问题，本文推出了KITScenes LongTail数据集，专注于长尾驾驶事件，并提供多视角视频、轨迹、高级指令及多语言推理轨迹。该数据集为多模态模型提供了一个新的基准，通过评估指令遵循和语义连贯性来衡量驾驶能力，并可用于研究不同推理形式对驾驶能力的影响。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>25. X-World: Controllable Ego-Centric Multi-Camera World Models for Scalable End-to-End Driving</strong><br><span>Chaoda Zheng, Sean Li, Jinhao Deng, Zhennan Wang, Shijia Chen, Liqiang Xiao, Ziheng Chi, Hongbin Lin, Kangjie Chen, Boyang Wang, Yu Zhang, Xianming Liu</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-03-20</div><div>2026-03-31</div><div><a href="http://arxiv.org/abs/2603.19979v2">2603.19979v2</a> / <a href="https://arxiv.org/pdf/2603.19979v2">PDF</a></div><div>cs.CV, cs.AI</div></td>
      <td style="width: 10%; vertical-align: top;">world model</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>在自动驾驶的端到端时代，视觉-语言-动作（VLA）策略直接将原始传感器数据流映射为驾驶动作，因此可扩展且可靠的评估变得愈发关键。然而，当前的评估流水线仍严重依赖现实世界道路测试，不仅成本高昂、场景覆盖有限，且难以复现。这些挑战推动了对真实世界模拟器的需求，该模拟器能够在给定建议动作下生成逼真的未来观测结果，同时在长时程内保持可控性和稳定性。我们提出了 X-World，这是一种基于动作条件的视觉-语言多相机生成式世界模型，可直接在视频空间模拟未来观测。给定同步的多视角相机历史序列和未来的动作序列，X-World 可以生成遵循指定动作的未来多相机视频流。为了确保场景推演的可复现性和可编辑性，X-World 进一步支持对动态交通主体和静态道路元素的可选控制，并保留了用于外观层面控制（如天气和时间）的文本提示接口。除了世界模拟，X-World 还通过在保持潜在动作和场景动力学的同时，对外观提示进行条件化，实现了视频风格转换。X-World 的核心是一个多视角潜在视频生成器，旨在明确鼓励在不同控制信号下保持跨视角的几何一致性和时间连贯性。实验表明，X-World 实现了高质量的多视角视频生成，具有以下特点：（i）极强的跨相机视角一致性，（ii）长时程推演中稳定的时间动力学，以及（iii）在严格遵循动作和忠实执行场景控制方面具有高可控性。这些特性使 X-World 成为可扩展和可复现评估的实用基础。</td>
      <td style="width: 20%; vertical-align: top;">针对自动驾驶评估中依赖实车测试导致的成本高、覆盖有限及难以复现等问题，本文提出了 X-World 多相机生成式世界模型。该方法通过动作条件和多视角一致性约束，能够生成受控的高质量多相机视频流，为自动驾驶系统的可扩展评估提供了一个稳健且可编辑的模拟基础。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>26. DriveVLM-RL: Neuroscience-Inspired Reinforcement Learning with Vision-Language Models for Safe and Deployable Autonomous Driving</strong><br><span>Zilin Huang, Zihao Sheng, Zhengyang Wan, Yansong Qu, Junwei You, Sicong Jiang, Sikai Chen</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-03-18</div><div>2026-03-18</div><div><a href="http://arxiv.org/abs/2603.18315v1">2603.18315v1</a> / <a href="https://arxiv.org/pdf/2603.18315v1">PDF</a></div><div>cs.RO, cs.AI, cs.CV</div></td>
      <td style="width: 10%; vertical-align: top;">VLM, RL</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>尽管端到端学习方法取得了快速进展，但确保自动驾驶汽车的决策安全仍然是一个根本性的挑战。传统的强化学习（RL）方法依赖于手动设计的奖励或稀疏的碰撞信号，这无法捕捉安全驾驶所需的丰富上下文理解，并使得在现实世界环境中不可避免地出现不安全的探索。尽管最近的视觉语言模型（VLM）提供了有前景的语义理解能力，但它们的高推理延迟和幻觉敏感性阻碍了其在实时车辆控制中的直接应用。为了解决这些限制，本文提出了 DriveVLM-RL，这是一个受神经科学启发的框架，通过双路径架构将 VLM 集成到强化学习中，以实现安全且可部署的自动驾驶。该框架将语义奖励学习分解为两条路径：一条是利用基于 CLIP 的对比语言目标进行持续空间安全评估的静态路径；另一条是利用轻量级检测器和大型 VLM 进行注意力门控多帧语义风险推理的动态路径。一种分层奖励合成机制将语义信号与车辆状态融合，而异步训练流水线则将高昂的 VLM 推理与环境交互解耦。所有 VLM 组件仅在离线训练期间使用，并在部署时移除，从而确保了实时可行性。在 CARLA 模拟器中的实验表明，该方法在碰撞避免、任务成功率以及跨不同交通场景的泛化能力方面均有显著提升，即便在没有显式碰撞惩罚的情况下也表现出强大的鲁棒性。这些结果证明，DriveVLM-RL 提供了一种在不影响实时可行性的前提下将基础模型集成到自动驾驶中的实用范式。</td>
      <td style="width: 20%; vertical-align: top;">针对传统强化学习在自动驾驶中奖励机制不足及 VLM 实时推理延迟的问题，本文提出了 DriveVLM-RL 框架。该方法通过受神经科学启发的双路径架构，在离线训练阶段利用 VLM 提供语义风险评估，并将训练好的模型部署于实时控制中，有效提升了自动驾驶的安全性和任务执行能力。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>27. Learning from Mistakes: Post-Training for Driving VLA with Takeover Data</strong><br><span>Yinfeng Gao, Deqing Liu, Qichao Zhang, Yupeng Zheng, Haochen Tian, Guang Li, Hangjun Ye, Long Chen, Da-Wei Ding, Dongbin Zhao</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-03-16</div><div>2026-03-16</div><div><a href="http://arxiv.org/abs/2603.14972v1">2603.14972v1</a> / <a href="https://arxiv.org/pdf/2603.14972v1">PDF</a></div><div>cs.RO</div></td>
      <td style="width: 10%; vertical-align: top;">RL</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>当前端到端自动驾驶中的视觉-语言-动作（VLA）范式依赖于静态数据集的离线训练，使其容易受到分布偏移的影响。近期的后训练方法通过使用接管数据来增强数据集以缓解这一问题，但存在两个主要局限性：监督仅限于接管时刻之后的阶段，导致策略的安全余量有限；被动偏好优化缺乏对最优性能的主动探索。在本文中，我们提出了TakeVLA，这是一种新颖的VLA后训练框架，通过两项互补的创新克服了这些缺点。首先，我们引入了接管前语言监督，使VLA能够从错误中主动学习。通过明确教授模型在易错情况下应采取的操作，我们培养了一种能及早预测危险并大幅扩大安全余量的预防性思维。其次，我们提出了场景梦想（Scenario Dreaming），这是一种在重建的接管场景中运行的强化微调范式，鼓励超越单纯偏好拟合的主动探索。在Bench2Drive基准测试上的实验表明，TakeVLA实现了最先进的闭环性能，驾驶得分超过了强基线模型SimLingo 4.93分，并且平均避撞时间（TTC）提高了11.76%，证明了其增强的安全余量。</td>
      <td style="width: 20%; vertical-align: top;">针对现有VLA模型在自动驾驶中存在的分布偏移和安全余量不足问题，本文提出了TakeVLA框架。通过引入接管前语言监督来强化预防性学习，并结合场景梦想强化微调范式进行主动探索，该方法在提升自动驾驶闭环性能和安全性方面取得了显著效果。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>28. Bridging Scene Generation and Planning: Driving with World Model via Unifying Vision and Motion Representation</strong><br><span>Xingtai Gui, Meijie Zhang, Tianyi Yan, Wencheng Han, Jiahao Gong, Feiyang Tan, Cheng-zhong Xu, Jianbing Shen</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-03-16</div><div>2026-03-16</div><div><a href="http://arxiv.org/abs/2603.14948v1">2603.14948v1</a> / <a href="https://arxiv.org/pdf/2603.14948v1">PDF</a></div><div>cs.CV</div></td>
      <td style="width: 10%; vertical-align: top;">world model</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>端到端自动驾驶旨在从原始传感器输入中生成安全且合理的规划策略。驾驶世界模型通过预测驾驶场景的未来演变，在学习丰富表征方面展现出巨大潜力。然而，现有的驾驶世界模型主要关注视觉场景表征，而运动表征并未被显式设计为可供规划器共享与继承，导致视觉场景生成优化与精确运动规划需求之间存在割裂。我们提出了WorldDrive，这是一个通过统一视觉和运动表征来耦合场景生成与实时规划的整体框架。我们首先引入了一种轨迹感知的驾驶世界模型，该模型以轨迹词汇为条件，强制视觉动态与运动意图之间的一致性，从而能够根据特定轨迹生成多样化且合理的未来场景。我们将视觉和运动编码器迁移到下游的多模态规划器，确保驾驶策略在场景生成预优化的成熟表征上运行。运动表征、视觉表征与自车状态之间的简单交互即可生成高质量的多模态轨迹。此外，为了利用世界模型的预见性，我们提出了一个未来感知奖励器，通过从冻结的世界模型中提取未来潜在表征，实时评估并选择最优轨迹。在NAVSIM、NAVSIM-v2和nuScenes基准测试上的广泛实验表明，WorldDrive在纯视觉方法中实现了领先的规划性能，同时保持了高保真的动作受控视频生成能力，为统一视觉和运动表征以实现鲁棒自动驾驶提供了有力证据。</td>
      <td style="width: 20%; vertical-align: top;">该论文针对现有自动驾驶世界模型在视觉生成与运动规划之间的表征割裂问题，提出了WorldDrive框架。通过统一视觉和运动表征，该方法不仅实现了受控的未来场景生成，还利用提取的未来潜在表征来优化实时轨迹规划。实验证明，该方法在保持高质量视频生成的同时，显著提升了端到端自动驾驶的规划性能。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>29. PerlAD: Towards Enhanced Closed-loop End-to-end Autonomous Driving with Pseudo-simulation-based Reinforcement Learning</strong><br><span>Yinfeng Gao, Qichao Zhang, Deqing Liu, Zhongpu Xia, Guang Li, Kun Ma, Guang Chen, Hangjun Ye, Long Chen, Da-Wei Ding, Dongbin Zhao</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-03-16</div><div>2026-03-16</div><div><a href="http://arxiv.org/abs/2603.14908v1">2603.14908v1</a> / <a href="https://arxiv.org/pdf/2603.14908v1">PDF</a></div><div>cs.RO, cs.CV</div></td>
      <td style="width: 10%; vertical-align: top;">world model, RL</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>基于模仿学习（IL）的端到端自动驾驶策略由于开环训练目标不足与实际驾驶需求之间的不匹配，在闭环执行中往往表现不佳。虽然强化学习（RL）通过奖励信号直接优化驾驶目标提供了一种解决方案，但基于渲染的训练环境存在渲染偏差，且因计算成本高而效率低下。为了克服这些挑战，我们提出了一种名为 PerlAD 的新型基于伪仿真的闭环端到端自动驾驶 RL 方法。PerlAD 基于离线数据集构建了一个在向量空间运行的伪仿真环境，实现了高效、免渲染的试错训练。为了弥合静态数据集与动态闭环环境之间的差距，PerlAD 引入了一个预测世界模型，能够根据自动驾驶车辆的计划生成响应式代理轨迹。此外，为了促进高效规划，PerlAD 利用了一种分层解耦规划器，将用于横向路径生成的 IL 与用于纵向速度优化的 RL 相结合。全面的实验结果表明，PerlAD 在 Bench2Drive 基准测试中实现了最先进的性能，在无需昂贵的在线交互的情况下，其驾驶得分超过了之前的端到端 RL 方法 10.29%。在 DOS 基准测试上的额外评估进一步证实了其在处理安全关键遮挡场景时的可靠性。</td>
      <td style="width: 20%; vertical-align: top;">针对端到端自动驾驶中模仿学习的闭环偏差和渲染驱动强化学习的计算成本问题，本文提出了 PerlAD 方法。该方法通过在向量空间中构建伪仿真环境并结合预测世界模型与分层解耦规划器，实现了高效的闭环训练。实验表明，PerlAD 在保持高性能的同时显著提升了自动驾驶系统在复杂和安全关键场景下的可靠性。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>30. AutoMoT: A Unified Vision-Language-Action Model with Asynchronous Mixture-of-Transformers for End-to-End Autonomous Driving</strong><br><span>Wenhui Huang, Songyan Zhang, Qihang Huang, Zhidong Wang, Zhiqi Mao, Collister Chua, Zhan Chen, Long Chen, Chen Lv</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-03-16</div><div>2026-03-18</div><div><a href="http://arxiv.org/abs/2603.14851v2">2603.14851v2</a> / <a href="https://arxiv.org/pdf/2603.14851v2">PDF</a></div><div>cs.CV, cs.RO</div></td>
      <td style="width: 10%; vertical-align: top;">VLM</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>将视觉语言模型（VLM）整合到端到端（E2E）自动驾驶（AD）系统中在提升场景理解能力方面展现出了前景。然而，现有的整合策略存在若干局限性：它们要么难以解决推理空间与动作空间之间的分布不匹配问题，要么未能充分利用预训练 VLM 的通用推理能力，要么在生成动作策略时产生大量的推理延迟，从而降低了驾驶性能。为了应对这些挑战，我们在本工作中提出了 AutoMoT，这是一个将推理和动作生成统一在单一视觉-语言-动作（VLA）模型中的端到端自动驾驶框架。我们的方法利用了具有联合注意力共享的混合 Transformer（MoT）架构，通过在不同任务频率下进行异步执行，在保留预训练 VLM 通用推理能力的同时，实现了高效的快慢推理。在开环和闭环设置下的多项基准测试表明，AutoMoT 达到了与最先进方法相媲美的性能。我们进一步探讨了预训练 VLM 在自动驾驶中的功能边界，研究了何时需要针对自动驾驶进行微调。结果表明，预训练 VLM 仅通过语义提示即可实现具有竞争力的多任务场景理解性能，而微调对于决策和轨迹规划等动作级任务仍然至关重要。</td>
      <td style="width: 20%; vertical-align: top;">针对现有自动驾驶模型中推理与动作生成脱节、效率低下等问题，本文提出了 AutoMoT 统一视觉-语言-动作模型。该方法采用异步混合 Transformer 架构，在保持预训练 VLM 推理能力的同时实现了高效的快慢推理。实验验证了该模型在场景理解和复杂驾驶任务中的竞争力，并明确了预训练模型在不同自动驾驶任务中是否需要微调的功能边界。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>31. WorldVLM: Combining World Model Forecasting and Vision-Language Reasoning</strong><br><span>Stefan Englmeier, Katharina Winter, Fabian B. Flohr</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-03-15</div><div>2026-03-17</div><div><a href="http://arxiv.org/abs/2603.14497v2">2603.14497v2</a> / <a href="https://arxiv.org/pdf/2603.14497v2">PDF</a></div><div>cs.CV, cs.RO</div></td>
      <td style="width: 10%; vertical-align: top;">VLM, world model</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>自动驾驶系统依赖于能够对高层场景上下文进行推理并准确预测周围环境动态的模型。视觉语言模型（VLMs）作为决策和场景理解的有力工具近期备受关注，并在上下文推理方面表现出强大的能力。然而，其有限的空间理解能力限制了它们作为端到端驾驶模型的有效性。世界模型（WMs）将环境动态内化以预测未来场景的演变。作为自我运动预测器和自动驾驶的基础模型，它们近期被探索为解决该领域关键挑战的一个有前景的方向，特别是在保持动态预测的同时增强泛化能力。为了利用基于上下文的决策和预测的互补优势，我们提出了WorldVLM：一种统一了VLM和WM的混合架构。在我们的设计中，高层VLM生成行为指令来引导驾驶WM，从而实现可解释且具有上下文意识的动作。我们评估了条件化策略，并提供了对混合设计挑战的见解。</td>
      <td style="width: 20%; vertical-align: top;">针对视觉语言模型在自动驾驶中空间理解能力不足的问题，本文提出了WorldVLM混合架构。该模型通过结合VLM的高层上下文决策能力与世界模型的未来场景预测能力，实现了更具解释性和环境感知力的自动驾驶决策。研究探讨了多种条件化策略，并分析了此类混合架构的设计难点。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>32. Fine-tuning is Not Enough: A Parallel Framework for Collaborative Imitation and Reinforcement Learning in End-to-end Autonomous Driving</strong><br><span>Zhexi Lian, Haoran Wang, Xuerun Yan, Weimeng Lin, Xianhong Zhang, Yongyu Chen, Jia Hu</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-03-14</div><div>2026-04-10</div><div><a href="http://arxiv.org/abs/2603.13842v3">2603.13842v3</a> / <a href="https://arxiv.org/pdf/2603.13842v3">PDF</a></div><div>cs.RO, cs.AI</div></td>
      <td style="width: 10%; vertical-align: top;">RL</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>端到端自动驾驶通常基于模仿学习（IL），但其性能受限于人类演示数据的质量。为了克服这一局限，现有方法常采用顺序微调的方式引入强化学习（RL）。然而，这种范式仍非最优：顺序的RL微调可能会导致策略漂移，并因过度依赖预训练的IL策略而遭遇性能瓶颈。针对这些问题，我们提出了PaIR-Drive，这是一个用于端到端自动驾驶的协作式模仿与强化学习并行框架。在训练阶段，PaIR-Drive将IL和RL拆分为两个具有无冲突训练目标的并行分支，实现了完全协同的优化，且应用新IL策略时无需重新训练RL。在推理阶段，RL利用IL策略进一步优化最终规划，从而实现超越IL先验知识的性能。此外，我们在RL分支中引入了一种树状轨迹神经采样器，用于优化分组相对策略（GRPO），从而增强了探索能力。在NAVSIMv1和v2基准测试上的广泛分析表明，PaIR-Drive在Transfuser和DiffusionDrive等IL基线基础上，达到了91.2 PDMS和87.9 EPDMS的竞争性表现。PaIR-Drive始终优于现有的RL微调方法，甚至能够纠正人类专家的次优行为。定性结果进一步证实，PaIR-Drive能够有效地探索并生成高质量的轨迹。</td>
      <td style="width: 20%; vertical-align: top;">针对端到端自动驾驶中模仿学习性能受限于人工演示及传统顺序微调导致的策略漂移问题，本文提出了PaIR-Drive并行框架。该方法将模仿学习与强化学习拆分为协作分支进行优化，并引入树状轨迹神经采样器增强探索能力。实验证明，该框架在保持竞争力的同时，能有效超越预训练策略的性能上限并纠正人工驾驶中的次优行为。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>33. FlowAD: Ego-Scene Interactive Modeling for Autonomous Driving</strong><br><span>Mingzhe Guo, Yixiang Yang, Chuanrong Han, Rufeng Zhang, Shirui Li, Ji Wan, Zhipeng Zhang</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-03-11</div><div>2026-03-11</div><div><a href="http://arxiv.org/abs/2603.13399v1">2603.13399v1</a> / <a href="https://arxiv.org/pdf/2603.13399v1">PDF</a></div><div>cs.CV</div></td>
      <td style="width: 10%; vertical-align: top;">VLM</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>高效的环境建模是自动驾驶的基础，支撑着从感知到规划的各项任务。然而，当前的范式往往未能充分考虑自身运动对观测的反馈，导致对驾驶过程的理解不完整，进而限制了规划能力。为了解决这一问题，我们引入了一种新颖的自我-场景交互建模范式。受人类识别机制的启发，该范式将自我-场景交互表示为相对于自动驾驶车辆的场景流。这一概念化过程允许在特征学习模式中对自我运动反馈进行建模，从而有效地利用现有的日志回放数据集，而非依赖场景模拟。我们专门提出了 FlowAD，这是一个用于自动驾驶的通用流基框架。在该框架中，自我引导的场景划分首先构建基础流单元以量化场景流。车辆的前进方向和转向速度直接决定了划分方式，从而反映了车辆自身的运动。随后，基于流单元进行空间和时间上的流预测，以建模场景流的动态，包括空间位移和时间变化。最终的任务感知增强策略利用所学习的时空流动态，通过对象和区域层面的策略使多种任务受益。我们还提出了一种新的“正确规划前帧数”（FCP）指标来评估场景理解能力。在开环和闭环评估中的实验证明了 FlowAD 在感知、端到端规划和视觉语言模型（VLM）分析方面的通用性和有效性。值得注意的是，FlowAD 在 nuScenes 数据集上将碰撞率降低了 19%，FCP 指标提升了 1.39 帧（60%），并在 Bench2Drive 上取得了 51.77 分的驾驶成绩，证明了其优越性。</td>
      <td style="width: 20%; vertical-align: top;">针对现有自动驾驶建模忽略车辆自身运动反馈的问题，本文提出了 FlowAD 范式，通过将交互建模为相对于自车的场景流来强化理解。该方法利用自车运动引导的场景划分及预测时空流动态，提升了感知、规划及分析任务的性能，并在 nuScenes 和 Bench2Drive 基准测试中展现出显著优势。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>34. Open-World Motion Forecasting</strong><br><span>Nicolas Schischka, Nikhil Gosala, B Ravi Kiran, Senthil Yogamani, Abhinav Valada</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-03-10</div><div>2026-03-16</div><div><a href="http://arxiv.org/abs/2603.09420v2">2603.09420v2</a> / <a href="https://arxiv.org/pdf/2603.09420v2">PDF</a></div><div>cs.CV, cs.AI, cs.RO</div></td>
      <td style="width: 10%; vertical-align: top;">VLM</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>运动预测旨在预测场景中动态主体的未来轨迹，使自动驾驶车辆能够有效地对场景演变进行推理。现有方法在封闭世界环境下运行，假设对象类别固定且具备高质量的感知能力。因此，它们在感知不完善且对象类别随时间演变的现实世界设置中表现不佳。本研究通过引入“开放世界运动预测”来弥补这一根本差距，这是一种新的设置，其中新对象类别随时间顺序引入，且直接从摄像机图像估计未来对象轨迹。我们通过提出首个端到端类别增量运动预测框架来解决此设置，旨在缓解灾难性遗忘，同时学习预测新引入的类别。当引入新类别时，我们的框架采用伪标签策略，首先为所有已知类别生成运动预测伪标签，然后由视觉-语言模型进行处理以过滤不一致和过度自信的预测。同时，我们的方法通过使用一种利用查询特征方差来采样具有信息丰富运动模式的先前序列的创新重放采样策略，进一步缓解了灾难性遗忘。在 nuScenes 和 Argoverse 2 数据集上的广泛评估表明，我们的方法成功抵御了灾难性遗忘，在保持对先前学习类别的性能的同时，提高了对新类别的适应性。此外，我们证明了该方法支持到现实世界驾驶的零样本迁移，并自然扩展到端到端类别增量规划，实现了完整自动驾驶系统的持续适应。</td>
      <td style="width: 20%; vertical-align: top;">本文针对现有运动预测方法难以应对现实世界中类别演变和感知缺陷的问题，提出了“开放世界运动预测”新设置。作者设计了一个端到端类别增量框架，结合伪标签过滤和基于查询特征方差的重放采样策略，有效克服了灾难性遗忘并提升了对新类别的适应能力。该方法不仅在基准数据集上表现出色，还支持零样本迁移及自动驾驶系统的持续增量更新。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>35. NaviDriveVLM: Decoupling High-Level Reasoning and Motion Planning for Autonomous Driving</strong><br><span>Ximeng Tao, Pardis Taghavi, Dimitar Filev, Reza Langari, Gaurav Pandey</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-03-09</div><div>2026-03-09</div><div><a href="http://arxiv.org/abs/2603.07901v1">2603.07901v1</a> / <a href="https://arxiv.org/pdf/2603.07901v1">PDF</a></div><div>cs.RO, cs.LG</div></td>
      <td style="width: 10%; vertical-align: top;">VLM</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>视觉语言模型（VLM）通过联合建模视觉观测、驾驶环境和基于语言的推理，已成为端到端自动驾驶（AD）的一个有前途的方向。然而，现有的基于VLM的系统在高层推理和运动规划之间面临权衡：大模型提供强大的语义理解能力但难以适应精确控制，而小VLM模型虽然可以高效微调，但通常表现出较弱的推理能力。我们提出了NaviDriveVLM，这是一个解耦框架，利用大规模的“导航器”和轻量级可训练的“驾驶员”将推理与动作生成分离开来。这种设计保留了推理能力，降低了训练成本，并为下游规划提供了显式且可解释的中间表示。在nuScenes基准测试上的实验表明，NaviDriveVLM在端到端运动规划方面优于大型VLM基准模型。</td>
      <td style="width: 20%; vertical-align: top;">针对现有端到端自动驾驶模型在高层推理能力与运动规划精确度之间的权衡问题，本研究提出了NaviDriveVLM框架，通过将大规模推理模块与轻量级运动规划模块解耦，实现了高效的动作生成。该方法不仅降低了训练成本，还提供了更具可解释性的中间表示，并在nuScenes基准测试中展现出优于大模型基线的性能。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>36. BEVLM: Distilling Semantic Knowledge from LLMs into Bird&#x27;s-Eye View Representations</strong><br><span>Thomas Monninger, Shaoyuan Xie, Qi Alfred Chen, Sihao Ding</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-03-06</div><div>2026-03-06</div><div><a href="http://arxiv.org/abs/2603.06576v1">2603.06576v1</a> / <a href="https://arxiv.org/pdf/2603.06576v1">PDF</a></div><div>cs.CV, cs.AI, cs.LG, cs.RO</div></td>
      <td style="width: 10%; vertical-align: top;">distillation</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>将大型语言模型（LLMs）集成到自动驾驶中，因其强大的推理和语义理解能力而备受关注，这对处理复杂决策和长尾场景至关重要。然而，现有方法通常将来自多视图和多帧图像的标记独立输入到LLM中，导致计算冗余和空间一致性受限。这种视觉处理的分离阻碍了精确的3D空间推理，且无法在不同视图间保持几何一致性。另一方面，从几何标注任务（如目标检测）中学习到的鸟瞰图（BEV）表示虽然提供了空间结构，但缺乏基础视觉编码器的语义丰富性。为了弥合这一差距，我们提出了BEVLM框架，将空间一致且经过语义蒸馏的BEV表示与LLM连接起来。通过大量实验，我们证明了BEVLM利用BEV特征作为统一输入，使LLM能够在跨视图驾驶场景中进行更有效的推理，准确率提高了46%。此外，通过将LLM的语义知识蒸馏到BEV表示中，BEVLM在安全关键场景下的闭环端到端驾驶性能显著提升了29%。</td>
      <td style="width: 20%; vertical-align: top;">本文针对现有自动驾驶模型在处理多视图数据时空间一致性不足且缺乏语义深度的问题，提出了BEVLM框架。该方法将经过语义蒸馏的鸟瞰图（BEV）表示与大语言模型结合，通过统一的BEV特征输入，显著增强了模型在复杂场景下的推理能力与端到端驾驶安全性。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>37. TADPO: Reinforcement Learning Goes Off-road</strong><br><span>Zhouchonghao Wu, Raymond Song, Vedant Mundheda, Luis E. Navarro-Serment, Christof Schoenborn, Jeff Schneider</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-03-06</div><div>2026-03-06</div><div><a href="http://arxiv.org/abs/2603.05995v1">2603.05995v1</a> / <a href="https://arxiv.org/pdf/2603.05995v1">PDF</a></div><div>cs.RO, cs.AI, cs.LG</div></td>
      <td style="width: 10%; vertical-align: top;">RL</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>越野自动驾驶在导航未经地图标注、动态多变且不确定的地形时面临严峻挑战，这要求系统具备高效的长程规划能力与自适应控制能力。强化学习（RL）通过从交互中直接学习控制策略提供了一种有前景的解决方案，但由于越野驾驶属于长程任务且奖励信号稀疏，标准强化学习方法难以直接应用。本文介绍了 TADPO，这是一种扩展了近端策略优化（PPO）的新型策略梯度公式，通过利用离线轨迹进行教师指导，并结合在线轨迹进行学生探索。基于此，我们开发了一种基于视觉的端到端越野驾驶强化学习系统，能够在大坡度和多障碍地形中实现高速行驶。我们在仿真环境中验证了该方法的性能，并实现了在全尺寸越野车上的零样本仿真到实机（sim-to-real）迁移。据我们所知，这是首次在全尺寸越野平台上部署基于强化学习的驾驶策略。</td>
      <td style="width: 20%; vertical-align: top;">针对越野驾驶长程任务中奖励稀疏和环境复杂的问题，本文提出了 TADPO 策略梯度方法，结合离线教师指导与在线学生探索以提升学习效率。该方法构建了一个端到端视觉强化学习系统，成功实现了全尺寸越野车辆在复杂地形下的高速驾驶及零样本实机迁移。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>38. Risk-Aware World Model Predictive Control for Generalizable End-to-End Autonomous Driving</strong><br><span>Jiangxin Sun, Feng Xue, Teng Long, Chang Liu, Jian-Fang Hu, Wei-Shi Zheng, Nicu Sebe</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-02-26</div><div>2026-02-26</div><div><a href="http://arxiv.org/abs/2602.23259v1">2602.23259v1</a> / <a href="https://arxiv.org/pdf/2602.23259v1">PDF</a></div><div>cs.CV, cs.AI, cs.RO</div></td>
      <td style="width: 10%; vertical-align: top;">world model, distillation</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>随着模仿学习（IL）和大规模驾驶数据集的发展，端到端自动驾驶（E2E-AD）近年来取得了巨大进步。目前，基于IL的方法已成为主流范式：模型依赖专家提供的标准驾驶行为，并通过最小化自身行为与专家行为之间的差异进行学习。然而，这种“仅模仿专家”的目标限制了泛化能力：当遇到专家演示分布之外的罕见或长尾场景时，模型由于缺乏先验经验往往会做出不安全的决策。这提出了一个根本性问题：端到端自动驾驶系统能否在没有专家行为监督的情况下做出可靠决策？为此，我们提出了一个名为“风险感知世界模型预测控制”（RaWMPC）的统一框架，旨在通过鲁棒控制解决这一泛化困境，且不依赖专家演示。在实践中，RaWMPC利用世界模型预测多种候选动作的后果，并通过显式的风险评估选择低风险动作。为了使世界模型具备预测危险驾驶行为后果的能力，我们设计了一种风险感知交互策略，系统地让世界模型接触危险行为，从而使灾难性后果变得可预测并可避免。此外，为了在测试时生成低风险候选动作，我们引入了一种自我评估蒸馏方法，将风险规避能力从训练好的世界模型蒸馏到一个生成式动作建议网络中，而无需任何专家演示。大量实验表明，RaWMPC在分布内和分布外场景下均优于最先进的方法，同时提供了卓越的决策可解释性。</td>
      <td style="width: 20%; vertical-align: top;">针对端到端自动驾驶模型在长尾场景中泛化能力不足的问题，本文提出了一种基于世界模型预测控制的RaWMPC框架。该方法通过引入风险感知交互策略和自我评估蒸馏机制，实现了在无需专家演示的情况下进行鲁棒的风险评估与动作决策。实验结果显示，该方法在提升决策安全性的同时，增强了模型在复杂场景下的泛化能力和可解释性。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>39. Unleashing the Potential of Diffusion Models for End-to-End Autonomous Driving</strong><br><span>Yinan Zheng, Tianyi Tan, Bin Huang, Enguang Liu, Ruiming Liang, Jianlin Zhang, Jianwei Cui, Guang Chen, Kun Ma, Hangjun Ye, Long Chen, Ya-Qin Zhang, Xianyuan Zhan, Jingjing Liu</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-02-26</div><div>2026-02-26</div><div><a href="http://arxiv.org/abs/2602.22801v1">2602.22801v1</a> / <a href="https://arxiv.org/pdf/2602.22801v1">PDF</a></div><div>cs.RO, cs.AI, cs.LG</div></td>
      <td style="width: 10%; vertical-align: top;">RL</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>扩散模型已成为机器人决策任务的热门选择，最近也被考虑用于解决自动驾驶任务。然而，它们在自动驾驶中的应用和评估仍局限于仿真或实验室环境。扩散模型在大型、复杂的现实世界场景（如端到端自动驾驶，E2E AD）中的全部潜力尚未得到充分探索。本研究基于海量的实车数据和道路测试，进行了系统且大规模的调查，旨在释放扩散模型作为 E2E AD 规划器的潜力。通过全面且严格控制的研究，我们确定了对 E2E 规划性能有显著影响的关键洞察，涵盖了扩散损失空间、轨迹表示和数据扩展。此外，我们还提供了一种有效的强化学习后训练策略，以进一步增强所学习规划器的安全性。由此产生的基于扩散的学习框架“超扩散规划器”（HDP）已部署在实车平台上，并在 6 种城市驾驶场景和 200 公里的真实世界测试中进行了评估，实现了比基准模型高出 10 倍的性能提升。我们的工作表明，当经过精心设计和训练时，扩散模型可以作为复杂真实世界自动驾驶任务中有效且可扩展的 E2E AD 规划器。</td>
      <td style="width: 20%; vertical-align: top;">针对端到端自动驾驶中扩散模型应用不足的问题，本研究通过大规模真实数据和严谨实验，分析了影响规划性能的关键因素并提出了超扩散规划器（HDP）。该方法引入了强化学习后训练策略以提升安全性，并在实车测试中实现了显著的性能提升，验证了扩散模型在复杂驾驶任务中的有效性和可扩展性。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>40. MindDriver: Introducing Progressive Multimodal Reasoning for Autonomous Driving</strong><br><span>Lingjun Zhang, Yujian Yuan, Changjie Wu, Xinyuan Chang, Xin Cai, Shuang Zeng, Linzhe Shi, Sijin Wang, Hang Zhang, Mu Xu</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-02-25</div><div>2026-02-25</div><div><a href="http://arxiv.org/abs/2602.21952v1">2602.21952v1</a> / <a href="https://arxiv.org/pdf/2602.21952v1">PDF</a></div><div>cs.CV</div></td>
      <td style="width: 10%; vertical-align: top;">VLM, RL</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>视觉语言模型（VLM）展现出强大的推理能力，在端到端自动驾驶系统中显示出应用前景。思维链（CoT）作为VLM广泛使用的推理策略，正面临严峻挑战。现有的文本思维链在文本语义空间与轨迹物理空间之间存在巨大鸿沟。尽管最近的方法利用未来图像代替文本作为CoT过程，但缺乏明确的规划导向目标引导来生成场景演化准确的图像。为了解决这些问题，我们创新性地提出了MindDriver，这是一个渐进式多模态推理框架，使VLM能够模仿人类的渐进式思维进行自动驾驶。MindDriver包含语义理解、语义到物理空间的想象以及物理空间的轨迹规划。为了在MindDriver中实现对齐的推理过程，我们开发了一个反馈引导的自动数据标注流水线，以生成对齐的多模态推理训练数据。此外，我们开发了一种渐进式强化微调方法，通过基于渐进式高层奖励的学习来优化对齐效果。MindDriver在nuScenes开环评估和Bench2Drive闭环评估中均表现出优越的性能。</td>
      <td style="width: 20%; vertical-align: top;">针对现有端到端自动驾驶中思维链缺乏物理空间对齐的问题，本文提出了MindDriver渐进式多模态推理框架。该方法通过引入语义到物理空间的想象及渐进式强化微调，实现了更准确的场景预测与轨迹规划。实验证明，该框架在开环和闭环自动驾驶评估中均取得了优异表现。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>41. Efficient and Explainable End-to-End Autonomous Driving via Masked Vision-Language-Action Diffusion</strong><br><span>Jiaru Zhang, Manav Gagvani, Can Cui, Juntong Peng, Ruqi Zhang, Ziran Wang</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-02-24</div><div>2026-02-24</div><div><a href="http://arxiv.org/abs/2602.20577v1">2602.20577v1</a> / <a href="https://arxiv.org/pdf/2602.20577v1">PDF</a></div><div>cs.CV</div></td>
      <td style="width: 10%; vertical-align: top;">VLM</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>大型语言模型（LLMs）和视觉语言模型（VLMs）已成为端到端自动驾驶的有前途的候选方案。然而，这些模型通常面临推理延迟、动作精度和可解释性方面的挑战。现有的自回归方法在逐个标记生成方面速度缓慢，而之前的基于扩散的规划器往往依赖于冗长且通用的语言标记，缺乏明确的几何结构。在本文中，我们提出了用于自动驾驶的掩码视觉-语言-动作扩散模型（MVLAD-AD），这是一个旨在通过掩码视觉-语言-动作扩散模型弥合高效规划与语义可解释性之间差距的新型框架。与强行将动作纳入语言空间的方法不同，我们引入了一种离散动作标记化策略，利用真实驾驶分布构建了运动学可行航点的紧凑码本。此外，我们提出了几何感知嵌入学习，以确保潜在空间中的嵌入近似物理几何度量。最后，引入了一种动作优先解码策略来优化轨迹生成。在 nuScenes 及其派生基准上的广泛实验表明，MVLAD-AD 在规划精度上实现了卓越的效率并优于最先进的自回归和扩散基线，同时提供了高保真且可解释的推理能力。</td>
      <td style="width: 20%; vertical-align: top;">针对现有自动驾驶模型推理延迟高和可解释性不足的问题，本文提出了 MVLAD-AD 框架。该方法通过离散动作标记化和几何感知嵌入学习，在实现高效轨迹规划的同时，提升了动作的精确度和推理的可解释性。实验结果验证了该模型在规划精度和效率上均优于主流的自回归和扩散基准方法。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>42. The Five Ws of Multi-Agent Communication: Who Talks to Whom, When, What, and Why -- A Survey from MARL to Emergent Language and LLMs</strong><br><span>Jingdi Chen, Hanqing Yang, Zongjun Liu, Carlee Joe-Wong</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-02-12</div><div>2026-02-12</div><div><a href="http://arxiv.org/abs/2602.11583v1">2602.11583v1</a> / <a href="https://arxiv.org/pdf/2602.11583v1">PDF</a></div><div>cs.AI, cs.LG</div></td>
      <td style="width: 10%; vertical-align: top;">distillation, RL</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>多智能体序贯决策驱动着从自动驾驶、机器人技术到协作式AI助手等诸多现实世界系统。在动态、部分可观测的环境中，通信往往是降低不确定性并实现协作的关键。本综述通过五个“W”来审视多智能体通信（MA-Comm）：谁与谁通信、通信的内容是什么、何时进行通信以及为何通信是有益的。这种框架提供了一种简洁的方式来连接不同研究领域间的思想。我们梳理了通信方法在三个主要范式中的演变。在多智能体强化学习（MARL）中，早期方法使用手工设计或隐式协议，随后转向针对奖励和控制进行优化的端到端学习通信。虽然取得了一定成功，但这些协议通常是特定于任务的且难以解释，这推动了新兴语言（EL）的研究，旨在使智能体通过交互发展出更具结构性或符号化的通信。然而，EL方法在基础性、泛化性和可扩展性方面仍面临挑战，这也促使近期人们开始关注大语言模型（LLM），它们为开放式环境下的推理、规划和协作引入了自然语言先验。在MARL、EL和基于LLM的系统之间，我们强调了不同的选择如何塑造通信设计、主要的权衡点在哪里以及哪些问题尚未解决。我们提炼了实用的设计模式和亟待解决的挑战，以支持未来结合学习、语言和控制的混合系统，从而实现可扩展且可解释的多智能体协作。</td>
      <td style="width: 20%; vertical-align: top;">该综述系统地分析了多智能体通信（MA-Comm）在多智能体强化学习、新兴语言及大语言模型三个范式下的演变与应用。文章通过“五个W”分析框架，探讨了通信设计的核心决策、权衡点及主要挑战，并为构建可扩展且可解释的协作系统提供了设计模式建议。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>43. ResWorld: Temporal Residual World Model for End-to-End Autonomous Driving</strong><br><span>Jinqing Zhang, Zehua Fu, Zelin Xu, Wenying Dai, Qingjie Liu, Yunhong Wang</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-02-11</div><div>2026-02-11</div><div><a href="http://arxiv.org/abs/2602.10884v1">2602.10884v1</a> / <a href="https://arxiv.org/pdf/2602.10884v1">PDF</a></div><div>cs.CV</div></td>
      <td style="width: 10%; vertical-align: top;">world model</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>世界模型在驾驶场景中的综合理解能力显著提高了端到端自动驾驶框架的规划精度。然而，对静态区域的冗余建模以及与轨迹之间缺乏深度交互，阻碍了世界模型发挥其全部效能。本文提出了时间残差世界模型（TR-World），旨在专注于动态目标建模。通过计算场景表示的时间残差，可以在不依赖检测和跟踪的情况下提取动态目标信息。TR-World 仅以时间残差作为输入，从而更精确地预测动态目标的未来空间分布。通过将该预测与当前 BEV 特征中包含的静态物体信息相结合，可以获得准确的未来 BEV 特征。此外，我们提出了未来引导轨迹细化（FGTR）模块，用于在先验轨迹（由当前场景表示预测）与未来 BEV 特征之间进行交互。该模块不仅能够利用未来路况来细化轨迹，还为未来 BEV 特征提供了稀疏的时空监督，以防止世界模型坍塌。在 nuScenes 和 NAVSIM 数据集上的综合实验表明，我们的方法（ResWorld）实现了最先进的规划性能。代码已开源。</td>
      <td style="width: 20%; vertical-align: top;">针对现有自动驾驶世界模型在动态建模上的冗余及与轨迹交互不足的问题，本文提出了 ResWorld 方法。该方法通过时间残差建模动态对象，并引入未来引导轨迹细化（FGTR）模块实现时空监督，显著提升了端到端自动驾驶的规划准确性。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>44. Found-RL: foundation model-enhanced reinforcement learning for autonomous driving</strong><br><span>Yansong Qu, Zihao Sheng, Zilin Huang, Jiancong Chen, Yuhao Luo, Tianyi Wang, Yiheng Feng, Samuel Labi, Sikai Chen</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-02-11</div><div>2026-02-11</div><div><a href="http://arxiv.org/abs/2602.10458v1">2602.10458v1</a> / <a href="https://arxiv.org/pdf/2602.10458v1">PDF</a></div><div>cs.AI, cs.LG</div></td>
      <td style="width: 10%; vertical-align: top;">VLM, distillation, RL</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>强化学习（RL）已成为端到端自动驾驶（AD）的主流范式。然而，RL 在复杂场景中存在样本效率低下和语义可解释性不足的问题。基础模型，特别是视觉语言模型（VLM），通过提供丰富的上下文感知知识可以缓解这一问题，但它们的高推理延迟阻碍了在高频 RL 训练循环中的部署。为了弥补这一差距，我们提出了 Found-RL，这是一个旨在利用基础模型高效增强自动驾驶 RL 的平台。其核心创新在于异步批量推理框架，它将繁重的 VLM 推理与仿真循环解耦，有效解决了延迟瓶颈以支持实时学习。我们引入了多种监督机制：价值边界正则化（VMR）和优势加权动作引导（AWAG），以有效地将专家级的 VLM 动作建议提取到 RL 策略中。此外，我们采用高吞吐量的 CLIP 进行稠密奖励塑造。我们通过条件对比动作对齐解决了 CLIP 的动态盲点问题，该方法将提示词条件化为离散的速度/命令，并从上下文特定的动作锚点评分中产生归一化的基于边界的奖励。Found-RL 提供了一个用于微调 VLM 集成的端到端流水线，并表明轻量级 RL 模型可以在维持实时推理（约 500 FPS）的同时，达到与十亿参数规模 VLM 相媲美的性能。</td>
      <td style="width: 20%; vertical-align: top;">针对自动驾驶强化学习中样本效率低和推理延迟高的问题，本文提出了 Found-RL 框架。该研究通过引入异步批量推理、新型奖励塑造及策略引导机制，成功将基础模型的先验知识蒸馏至轻量级 RL 模型中。实验表明，该方法在保持高实时推理性能的同时，实现了接近大型视觉语言模型的驾驶表现。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>45. DriveWorld-VLA: Unified Latent-Space World Modeling with Vision-Language-Action for Autonomous Driving</strong><br><span>Feiyang jia, Lin Liu, Ziying Song, Caiyan Jia, Hangjun Ye, Xiaoshuai Hao, Long Chen</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-02-06</div><div>2026-02-06</div><div><a href="http://arxiv.org/abs/2602.06521v1">2602.06521v1</a> / <a href="https://arxiv.org/pdf/2602.06521v1">PDF</a></div><div>cs.CV, cs.RO</div></td>
      <td style="width: 10%; vertical-align: top;">world model</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>端到端（E2E）自动驾驶近年来在整合视觉-语言-动作（VLA）与世界模型以提升决策能力和前瞻性想象力方面备受关注。然而，现有方法由于潜在状态共享不足，无法在单一架构内有效统一未来场景演变与动作规划，限制了视觉想象力对动作决策的影响。为解决这一局限，我们提出了 DriveWorld-VLA，这是一个在潜在空间内统一世界建模与规划的新颖框架。通过在表征层面深度整合 VLA 与世界模型，使 VLA 规划器能够直接从整体场景演变建模中获益，并减少对密集标注监督的依赖。此外，DriveWorld-VLA 将世界模型的潜在状态作为 VLA 规划器的核心决策状态，帮助规划器评估候选动作如何影响未来场景演变。通过在潜在空间内完整执行世界建模，DriveWorld-VLA 支持特征层面的、可控的动作条件化想象，避免了昂贵的像素级演化。广泛的开环和闭环评估验证了 DriveWorld-VLA 的有效性，其在 NAVSIMv1 上达到 91.3 PDMS，在 NAVSIMv2 上达到 86.8 EPDMS，在 nuScenes 上达到 0.16 的 3 秒平均碰撞率，实现了最先进的性能。</td>
      <td style="width: 20%; vertical-align: top;">针对现有自动驾驶方法中世界建模与动作规划整合不足的问题，论文提出了 DriveWorld-VLA 框架，在潜在空间内实现了视觉-语言-动作与世界模型的深度融合。该方法利用世界模型的潜在状态增强规划器的决策能力，并支持高效的可控动作预测。实验结果表明，该模型在多个自动驾驶基准测试中均达到了最优性能。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>46. AppleVLM: End-to-end Autonomous Driving with Advanced Perception and Planning-Enhanced Vision-Language Models</strong><br><span>Yuxuan Han, Kunyuan Wu, Qianyi Shao, Renxiang Xiao, Zilu Wang, Cansen Jiang, Yi Xiao, Liang Hu, Yunjiang Lou</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-02-04</div><div>2026-02-04</div><div><a href="http://arxiv.org/abs/2602.04256v1">2602.04256v1</a> / <a href="https://arxiv.org/pdf/2602.04256v1">PDF</a></div><div>cs.RO, cs.AI</div></td>
      <td style="width: 10%; vertical-align: top;">VLM</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>端到端自动驾驶已成为一种将感知、决策和控制集成在统一学习框架中的有前景的范式。最近，视觉语言模型（VLM）因其在增强端到端驾驶模型在多样化和未知场景下的鲁棒性和泛化能力方面的潜力而备受关注。然而，现有的基于VLM的方法仍面临车道感知不佳、语言理解偏差以及处理边缘情况困难等挑战。为了解决这些问题，我们提出了AppleVLM，这是一种用于稳健端到端驾驶的增强型感知与规划VLM模型。AppleVLM引入了一种新颖的视觉编码器和规划策略编码器来提升感知与决策能力。首先，视觉编码器利用可变形Transformer机制融合来自多个时间步的多视图图像的时空信息，增强了对相机变化的鲁棒性，并促进了在不同车辆平台上的可扩展部署。其次，与传统的基于VLM的方法不同，AppleVLM引入了一种专门的规划模态，用于编码明确的鸟瞰图（BEV）空间信息，减轻了导航指令中的语言偏差。最后，通过分层思维链微调的VLM解码器将视觉、语言和规划特征进行整合，输出稳健的驾驶路点。我们在两个CARLA基准测试的闭环实验中评估了AppleVLM，实现了最先进的驾驶性能。此外，我们将AppleVLM部署在AGV平台上，并成功展示了其在复杂户外环境下的真实世界端到端自动驾驶能力。</td>
      <td style="width: 20%; vertical-align: top;">针对现有VLM自动驾驶模型在感知和规划上的不足，本文提出了AppleVLM模型。该方法通过引入时空信息融合的视觉编码器和BEV规划策略编码器，并结合分层思维链微调，显著提升了驾驶决策的鲁棒性。在CARLA模拟器和真实AGV平台上的实验证明，该方法实现了领先的端到端驾驶性能。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>47. Natural Language Instructions for Scene-Responsive Human-in-the-Loop Motion Planning in Autonomous Driving using Vision-Language-Action Models</strong><br><span>Angel Martinez-Sanchez, Parthib Roy, Ross Greer</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-02-04</div><div>2026-02-04</div><div><a href="http://arxiv.org/abs/2602.04184v1">2602.04184v1</a> / <a href="https://arxiv.org/pdf/2602.04184v1">PDF</a></div><div>cs.CV, cs.AI, cs.LG, cs.RO</div></td>
      <td style="width: 10%; vertical-align: top;">VLM</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>指令导向的自动驾驶要求车辆在运动前理解乘客的语言意图以指导轨迹规划。然而，大多数现有的指令遵循规划器依赖于模拟或固定的命令词汇，限制了其在现实世界中的泛化能力。doScenes 是第一个将自由形式的指令（具备指代性）与 nuScenes 真实路况运动数据相关联的现实世界数据集，从而实现了基于指令的轨迹规划。在本文中，我们将 OpenEMMA（一个基于多模态大模型、输入前视摄像头视图和自身状态并输出10步速度-曲率轨迹的端到端驾驶框架）适配到该场景中，提出了一个基于 doScenes 的可复现指令条件基准，并研究了人类指令提示对预测驾驶行为的影响。我们将 doScenes 指令作为乘客风格的提示整合进 OpenEMMA 的视觉-语言接口，从而在生成轨迹前实现语言条件化控制。通过在849个标注场景中利用平均位移误差（ADE）进行评估，我们发现指令条件化通过防止极端基准故障显著增强了鲁棒性，使平均 ADE 降低了 98.7%。在剔除这些异常值后，指令仍能影响轨迹的对齐程度，良好的提示语可使 ADE 进一步提升多达 5.1%。基于此分析，我们讨论了对 OpenEMMA 框架而言什么样的指令是“好的”。我们发布了评估提示词和脚本，旨在为指令感知规划建立可复现的基准。</td>
      <td style="width: 20%; vertical-align: top;">本文针对自动驾驶中指令导向轨迹规划泛化能力不足的问题，利用 doScenes 数据集将自由形式的乘客指令引入 OpenEMMA 视觉-语言端到端规划框架。通过将指令作为条件输入，该方法显著减少了极端运动规划错误，并验证了高质量语言提示对于提升轨迹预测准确性的有效性。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>48. HERMES: A Holistic End-to-End Risk-Aware Multimodal Embodied System with Vision-Language Models for Long-Tail Autonomous Driving</strong><br><span>Weizhe Tang, Junwei You, Jiaxi Liu, Zhaoyi Wang, Rui Gan, Zilin Huang, Feng Wei, Bin Ran</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-02-01</div><div>2026-02-01</div><div><a href="http://arxiv.org/abs/2602.00993v1">2602.00993v1</a> / <a href="https://arxiv.org/pdf/2602.00993v1">PDF</a></div><div>cs.RO, cs.AI</div></td>
      <td style="width: 10%; vertical-align: top;">VLM</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>端到端自动驾驶模型越来越多地受益于大视觉-语言模型以实现语义理解，但在长尾条件下确保安全且精确的操作仍然具有挑战性。这些挑战在长尾混合交通场景中尤为突出，自动驾驶车辆必须在复杂且不确定的条件下与包括人类驾驶车辆及弱势道路使用者在内的异构道路参与者进行交互。本文提出了HERMES，一个整体式风险感知端到端多模态驾驶框架，旨在将明确的长尾风险提示注入轨迹规划中。HERMES采用基础模型辅助的标注流水线，生成结构化的长尾场景上下文和长尾规划上下文，捕捉以危险为中心的提示以及操纵意图和安全偏好，并利用这些信号指导端到端规划。HERMES进一步引入了一个三模态驾驶模块，融合了多视角感知、历史运动线索和语义引导，确保在长尾场景下实现风险感知的精确轨迹规划。在真实世界长尾数据集上的实验表明，HERMES在长尾混合交通场景下的表现始终优于现有的端到端和基于VLM的基准模型。消融实验验证了关键组件的互补贡献。</td>
      <td style="width: 20%; vertical-align: top;">针对自动驾驶在长尾混合交通场景中难以处理复杂风险的问题，本文提出了HERMES框架。该框架通过引入基础模型辅助的上下文标注生成机制和三模态驾驶模块，将风险提示有效融入端到端轨迹规划过程。实验证明，该方法在提升长尾场景下的驾驶安全性和轨迹规划准确度方面优于现有主流方法。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>49. Drive-JEPA: Video JEPA Meets Multimodal Trajectory Distillation for End-to-End Driving</strong><br><span>Linhan Wang, Zichong Yang, Chen Bai, Guoxiang Zhang, Xiaotong Liu, Xiaoyin Zheng, Xiao-Xiao Long, Chang-Tien Lu, Cheng Lu</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-01-29</div><div>2026-01-29</div><div><a href="http://arxiv.org/abs/2601.22032v1">2601.22032v1</a> / <a href="https://arxiv.org/pdf/2601.22032v1">PDF</a></div><div>cs.CV</div></td>
      <td style="width: 10%; vertical-align: top;">world model, distillation</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>端到端自动驾驶正越来越多地利用自监督视频预训练来学习可迁移的规划表征。然而，目前针对场景理解的视频世界模型预训练所带来的改进仍然有限。这种局限性因驾驶环境固有的模糊性而加剧：每个场景通常仅提供单一的人类轨迹，使得学习多模态行为变得困难。在这项工作中，我们提出了 Drive-JEPA，这是一个将视频联合嵌入预测架构（V-JEPA）与多模态轨迹蒸馏相结合的端到端驾驶框架。首先，我们将 V-JEPA 应用于端到端驾驶，通过在大规模驾驶视频上预训练 ViT 编码器，生成与轨迹规划对齐的预测性表征。其次，我们引入了一种以提案为中心的规划器，通过蒸馏模拟器生成的多种轨迹以及人类轨迹，并结合动量感知选择机制，以促进稳定且安全的驾驶行为。在 NAVSIM 上的评估表明，在无感知条件下，结合简单 Transformer 解码器的 V-JEPA 表征比现有方法提升了 3 个 PDMS。完整的 Drive-JEPA 框架在 v1 版本上达到 93.3 PDMS，在 v2 版本上达到 87.8 EPDMS，创下了新的技术水平。</td>
      <td style="width: 20%; vertical-align: top;">针对端到端驾驶中场景理解能力受限及行为多模态学习困难的问题，本文提出了 Drive-JEPA 框架。该方法通过将 V-JEPA 预训练表征与多模态轨迹蒸馏规划器相结合，在 NAVSIM 基准测试中实现了性能提升，创造了新的最优结果。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>50. Generative Scenario Rollouts for End-to-End Autonomous Driving</strong><br><span>Rajeev Yasarla, Deepti Hegde, Shizhong Han, Hsin-Pai Cheng, Yunxiao Shi, Meysam Sadeghigooghari, Shweta Mahajan, Apratim Bhattacharyya, Litian Liu, Risheek Garrepalli, Thomas Svantesson, Fatih Porikli, Hong Cai</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-01-16</div><div>2026-01-16</div><div><a href="http://arxiv.org/abs/2601.11475v1">2601.11475v1</a> / <a href="https://arxiv.org/pdf/2601.11475v1">PDF</a></div><div>cs.CV</div></td>
      <td style="width: 10%; vertical-align: top;">RL</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>视觉-语言-动作（VLA）模型正逐渐成为端到端自动驾驶系统中极为有效的规划模型。然而，目前的研究大多依赖于稀疏轨迹标注的模仿学习，且未能充分利用其作为生成模型的能力。我们提出了生成式场景推演（GeRo），这是一个为 VLA 模型设计的即插即用框架，通过自回归推演策略联合执行基于语言的未来交通场景规划与生成。首先，VLA 模型在规划、运动和语言任务的监督下进行训练，将自车和智能体动态编码为潜在标记，以促进文本对齐的生成。接下来，GeRo 执行语言条件的自回归生成。在给定多视角图像、场景描述和自车动作问题的情况下，它生成未来的潜在标记和文本响应以指导长时程推演。推演一致性损失利用真值或伪标签稳定预测，减轻漂移并保持文本与动作的对齐。该设计使 GeRo 能够执行时间一致、语言驱动的推演，从而支持长时程推理和多智能体规划。在 Bench2Drive 评测中，GeRo 的驾驶评分和成功率分别提升了 15.7 和 26.2。通过将强化学习与生成式推演相结合，GeRo 在闭环和开环性能上均达到了领先水平，并展现出强大的零样本鲁棒性。这些结果凸显了生成式、语言条件推理作为构建更安全、更具可解释性端到端自动驾驶系统的基础潜力。</td>
      <td style="width: 20%; vertical-align: top;">针对当前端到端自动驾驶中 VLA 模型未能充分发挥生成潜力的问题，本文提出了 GeRo 框架，通过自回归推演策略实现基于语言的未来场景预测与规划。该方法结合了推演一致性损失与强化学习，在长时程推理和多智能体场景中显著提升了驾驶性能与模型鲁棒性。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>51. SGDrive: Scene-to-Goal Hierarchical World Cognition for Autonomous Driving</strong><br><span>Jingyu Li, Junjie Wu, Dongnan Hu, Xiangkai Huang, Bin Sun, Zhihui Hao, Xianpeng Lang, Xiatian Zhu, Li Zhang</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-01-09</div><div>2026-01-12</div><div><a href="http://arxiv.org/abs/2601.05640v2">2601.05640v2</a> / <a href="https://arxiv.org/pdf/2601.05640v2">PDF</a></div><div>cs.CV</div></td>
      <td style="width: 10%; vertical-align: top;">VLM</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>近期的端到端自动驾驶方法利用视觉语言模型（VLM）来增强复杂驾驶场景中的规划能力。然而，VLM 本质上是通用模型，缺乏对三维时空中驾驶特定推理的专业理解。当应用于自动驾驶时，这些模型难以建立结构化的时空表征，从而无法捕捉对安全轨迹规划至关重要的几何关系、场景上下文和运动模式。为了解决这些局限性，我们提出了 SGDrive，这是一个围绕驾驶特定知识层次结构显式构建 VLM 表征学习的新框架。SGDrive 基于预训练的 VLM 主干，将驾驶理解分解为模拟人类驾驶认知的“场景-智能体-目标”层次结构：驾驶员首先感知整体环境（场景上下文），然后关注安全关键的智能体及其行为，最后在执行动作前制定短期目标。这种层次化分解提供了通用 VLM 所缺乏的结构化时空表征，将多层次信息集成到紧凑而全面的格式中，用于轨迹规划。在 NAVSIM 基准测试上的大量实验表明，SGDrive 在 PDMS 和 EPDMS 上均达到了仅使用摄像头方法的最先进性能，验证了层次化知识结构化对于将通用 VLM 适配到自动驾驶领域的有效性。</td>
      <td style="width: 20%; vertical-align: top;">针对通用视觉语言模型在自动驾驶领域缺乏结构化时空理解的问题，本文提出了 SGDrive 框架。该方法通过引入“场景-智能体-目标”的层次化知识结构，将驾驶认知过程分解，有效提升了复杂场景下的轨迹规划能力。实验证明，该方法在 NAVSIM 基准测试中实现了纯视觉自动驾驶任务的最优性能。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>52. FLARE: Learning Future-Aware Latent Representations from Vision-Language Models for Autonomous Driving</strong><br><span>Chengen Xie, Chonghao Sima, Tianyu Li, Bin Sun, Junjie Wu, Zhihui Hao, Hongyang Li</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-01-09</div><div>2026-03-09</div><div><a href="http://arxiv.org/abs/2601.05611v2">2601.05611v2</a> / <a href="https://arxiv.org/pdf/2601.05611v2">PDF</a></div><div>cs.CV</div></td>
      <td style="width: 10%; vertical-align: top;">VLM</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>尽管视觉语言模型（VLM）为端到端自动驾驶提供了丰富的世界知识，但当前方法严重依赖劳动密集型的语言标注（如视觉问答）来连接感知与控制。这种范式在离散语言标记与连续驾驶轨迹之间存在根本性的不匹配，往往导致次优的控制策略以及对预训练知识的低效利用。为了解决这些挑战，我们提出了FLARE（未来感知潜表征），这是一个在无需语言监督的情况下激活预训练VLM视觉语义能力的创新框架。我们没有采用与文本对齐的方式，而是引入了一种自监督的未来特征预测目标。该机制迫使模型直接在潜空间中预判场景动态和自车运动，从而能够从大规模无标签轨迹数据中学习稳健的驾驶表征。此外，我们将组相对策略优化（GRPO）集成到规划过程中，以提升决策质量。在NAVSIM基准测试上的广泛实验表明，FLARE达到了最先进的性能，验证了通过预测性自监督而非显式语言生成来利用VLM知识的有效性。</td>
      <td style="width: 20%; vertical-align: top;">针对端到端自动驾驶中依赖语言标注的局限，该论文提出了FLARE框架，通过引入自监督的未来特征预测目标，使模型能在无语言监督下从大规模轨迹数据中学习驾驶表征。该方法利用未来状态预测和组相对策略优化，在NAVSIM基准测试中实现了最优的决策性能。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>53. FROST-Drive: Scalable and Efficient End-to-End Driving with a Frozen Vision Encoder</strong><br><span>Zeyu Dong, Yimin Zhu, Yu Wu, Yu Sun</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2026-01-06</div><div>2026-01-06</div><div><a href="http://arxiv.org/abs/2601.03460v1">2601.03460v1</a> / <a href="https://arxiv.org/pdf/2601.03460v1">PDF</a></div><div>cs.CV, cs.AI</div></td>
      <td style="width: 10%; vertical-align: top;">VLM</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>自动驾驶中的端到端（E2E）模型旨在将传感器输入直接映射为控制指令，但其对新颖且复杂场景的泛化能力仍是一项关键挑战。在驾驶数据集上对视觉编码器进行全量微调的常规做法，可能会因模型过度拟合训练数据而限制其泛化能力。本研究对这种训练范式提出了质疑，并提出了FROST-Drive，这是一种旨在保留和利用视觉语言模型（VLM）预训练视觉编码器强大泛化能力的新型E2E架构。通过冻结编码器权重，我们的方法将VLM中丰富的通用世界知识直接迁移至驾驶任务中。模型架构结合了该冻结编码器、用于多模态融合的Transformer适配器以及用于生成平滑航点的GRU解码器。此外，我们引入了一种专门设计的自定义损失函数，用于直接优化评估者反馈分数（RFS），该指标优先考虑鲁棒的轨迹规划。我们在精心筛选长尾场景的大规模数据集Waymo Open E2E上进行了大量实验，结果表明我们的冻结编码器方法显著优于采用全量微调的模型。研究结果提供了有力证据，表明保留高性能VLM的广泛知识比高强度的领域特定适应，在实现鲁棒且可泛化的驾驶性能方面更为有效。这为开发能够更好地处理真实世界应用场景复杂性的视觉模型提供了新途径。</td>
      <td style="width: 20%; vertical-align: top;">针对端到端自动驾驶模型在微调过程中容易过拟合训练数据的问题，本文提出了FROST-Drive方法，通过冻结预训练视觉语言模型的编码器来保留其泛化知识。该方法结合了多模态适配器和针对轨迹规划优化的损失函数，在长尾场景数据集上的表现显著优于全量微调方案，证明了利用预训练模型通用知识的有效性。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>54. Dichotomous Diffusion Policy Optimization</strong><br><span>Ruiming Liang, Yinan Zheng, Kexin Zheng, Tianyi Tan, Jianxiong Li, Liyuan Mao, Zhihao Wang, Guang Chen, Hangjun Ye, Jingjing Liu, Jinqiao Wang, Xianyuan Zhan</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2025-12-31</div><div>2026-02-01</div><div><a href="http://arxiv.org/abs/2601.00898v2">2601.00898v2</a> / <a href="https://arxiv.org/pdf/2601.00898v2">PDF</a></div><div>cs.LG, cs.RO</div></td>
      <td style="width: 10%; vertical-align: top;">RL</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>基于扩散的策略因其卓越的表达能力和推理过程中的可控生成，在解决各类决策任务中日益受到欢迎。然而，使用强化学习（RL）有效训练大型扩散策略仍然具有挑战性。现有方法要么因直接最大化价值目标而导致训练不稳定，要么因依赖粗糙的高斯似然近似（需要大量极小的去噪步骤）而面临计算问题。在这项工作中，我们提出了DIPOLE（二分扩散策略改进），这是一种专为稳定且可控的扩散策略优化设计的新型强化学习算法。我们首先重新审视了强化学习中的KL正则化目标，该目标为扩散策略提取提供了理想的加权回归目标，但往往难以平衡贪婪性与稳定性。随后，我们制定了一种贪婪策略正则化方案，自然地将最优策略分解为一对稳定学习的二分策略：一个旨在最大化奖励，另一个侧重于最小化奖励。在这种设计下，推理过程中可以通过线性组合二分策略的分数来生成优化动作，从而实现对贪婪程度的灵活控制。在ExORL和OGBench的离线及离线到在线强化学习环境下的评估证明了我们方法的有效性。我们还利用DIPOLE训练了一个用于端到端自动驾驶（AD）的大型视觉-语言-动作（VLA）模型，并在大规模真实世界AD基准NAVSIM上进行了评估，突显了其在复杂真实世界应用中的潜力。</td>
      <td style="width: 20%; vertical-align: top;">针对大型扩散策略在强化学习训练中存在的不稳定和计算效率问题，本文提出了DIPOLE算法。该方法通过将最优策略分解为最大化和最小化奖励的二分策略，实现了对策略贪婪程度的灵活与稳定控制。实验表明，该方法在离线强化学习基准及自动驾驶场景中均表现出优异的性能。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>55. Spatial-aware Vision Language Model for Autonomous Driving</strong><br><span>Weijie Wei, Zhipeng Luo, Ling Feng, Venice Erin Liong</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2025-12-30</div><div>2025-12-30</div><div><a href="http://arxiv.org/abs/2512.24331v1">2512.24331v1</a> / <a href="https://arxiv.org/pdf/2512.24331v1">PDF</a></div><div>cs.CV</div></td>
      <td style="width: 10%; vertical-align: top;">VLM</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>尽管视觉语言模型（VLM）通过利用语言模型中嵌入的常识，在端到端自动驾驶方面展现出巨大潜力，但它们对二维图像线索的依赖在复杂场景理解和决策制定方面形成了安全和可靠性的关键瓶颈。当前的图像方法难以进行精确的度量空间推理和几何推断，导致了不可靠的驾驶策略。为了弥补这一差距，我们提出了 LVLDrive（激光雷达-视觉-语言），这是一种旨在通过引入激光雷达点云作为额外输入模态，从而利用稳健的三维度量空间理解来升级现有 VLM 的新框架。一个关键挑战在于减轻迥异的三维数据对预训练 VLM 造成的灾难性干扰。为此，我们引入了一种渐进式融合 Q-Former，它能够逐步注入激光雷达特征，确保 VLM 现有知识库的稳定性和完整性。此外，我们开发了一个空间感知问答（SA-QA）数据集，旨在明确教导模型具备高级的三维感知和推理能力。在驾驶基准测试上的广泛实验表明，与纯视觉模型相比，LVLDrive 在场景理解、度量空间感知和可靠的驾驶决策制定方面实现了优越的性能。我们的工作突显了显式三维度量数据对于构建可信的基于 VLM 的自动驾驶系统的必要性。</td>
      <td style="width: 20%; vertical-align: top;">针对现有视觉语言模型在自动驾驶中空间推理能力不足的问题，本文提出了 LVLDrive 框架，通过引入激光雷达点云模态并设计渐进式融合 Q-Former，在保持模型原有知识的基础上增强了三维感知。此外，作者构建了空间感知问答数据集，实验证明该方法在场景理解与驾驶决策的准确性及可靠性上均优于纯视觉方案。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>56. ColaVLA: Leveraging Cognitive Latent Reasoning for Hierarchical Parallel Trajectory Planning in Autonomous Driving</strong><br><span>Qihang Peng, Xuesong Chen, Chenye Yang, Shaoshuai Shi, Hongsheng Li</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2025-12-28</div><div>2026-02-27</div><div><a href="http://arxiv.org/abs/2512.22939v3">2512.22939v3</a> / <a href="https://arxiv.org/pdf/2512.22939v3">PDF</a></div><div>cs.CV</div></td>
      <td style="width: 10%; vertical-align: top;">VLM</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>自动驾驶需要从复杂的多模态输入中生成安全可靠的轨迹。传统的模块化流水线将感知、预测和规划分离开来，而近期的端到端（E2E）系统则联合学习这些过程。视觉语言模型（VLMs）通过引入跨模态先验和常识推理进一步丰富了这一范式，但当前基于 VLM 的规划器面临三个关键挑战：(i) 离散文本推理与连续控制之间的不匹配，(ii) 自回归思维链解码导致的高延迟，以及 (iii) 低效或非因果规划器限制了实时部署。我们提出了 ColaVLA，这是一个统一的视觉-语言-动作框架，它将推理从文本迁移到一个统一的潜空间，并将其与分层并行轨迹解码器耦合。认知潜推理器通过自我适应选择和仅两次 VLM 前向传播，将场景理解压缩为紧凑的、面向决策的元动作嵌入。分层并行规划器随后在单次前向传播中生成多尺度、因果一致的轨迹。这些组件共同保留了 VLM 的泛化性和可解释性，同时实现了高效、准确且安全的轨迹生成。在 nuScenes 基准测试上的实验表明，ColaVLA 在开环和闭环设置中均达到了最先进的性能，并具有良好的效率和稳健性。</td>
      <td style="width: 20%; vertical-align: top;">该研究针对现有基于视觉语言模型的自动驾驶规划器在实时性、连续控制和推理效率方面的不足，提出了 ColaVLA 框架。该框架利用认知潜推理器将场景理解压缩为元动作嵌入，并结合分层并行轨迹解码器实现高效的轨迹生成。实验结果表明，该方法在保持模型泛化性和可解释性的同时，显著提升了自动驾驶系统在基准测试中的性能和部署效率。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>57. WorldRFT: Latent World Model Planning with Reinforcement Fine-Tuning for Autonomous Driving</strong><br><span>Pengxuan Yang, Ben Lu, Zhongpu Xia, Chao Han, Yinfeng Gao, Teng Zhang, Kun Zhan, XianPeng Lang, Yupeng Zheng, Qichao Zhang</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2025-12-22</div><div>2025-12-22</div><div><a href="http://arxiv.org/abs/2512.19133v1">2512.19133v1</a> / <a href="https://arxiv.org/pdf/2512.19133v1">PDF</a></div><div>cs.RO, cs.CV</div></td>
      <td style="width: 10%; vertical-align: top;">world model, RL</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>潜在世界模型通过时间自监督学习增强了场景表示，为端到端自动驾驶提供了一种无需感知标注的范式。然而，以重构为导向的表示学习将感知与规划任务耦合，导致规划任务的优化次优。为了应对这一挑战，我们提出了WorldRFT，一个面向规划的潜在世界模型框架。该框架通过分层规划分解和局部感知交互细化机制，将场景表示学习与规划对齐，并辅以强化学习微调（RFT）以增强安全关键策略的性能。具体而言，WorldRFT集成了一个视觉几何基础模型以提升3D空间感知，采用分层规划任务分解引导表示优化，并利用局部感知迭代细化导出面向规划的驾驶策略。此外，我们引入了组相对策略优化（GRPO），通过轨迹高斯化和碰撞感知奖励来微调驾驶策略，从而系统性地提高了安全性。WorldRFT在开环nuScenes和闭环NavSim基准测试中均达到了最先进（SOTA）水平。在nuScenes上，它将碰撞率降低了83%（从0.30%降至0.05%）。在NavSim上，仅使用纯视觉传感器输入，其性能即与基于激光雷达的SOTA方法DiffusionDrive相当（PDMS得分为87.8对88.1）。</td>
      <td style="width: 20%; vertical-align: top;">针对现有世界模型因重构导向导致规划性能受限的问题，本文提出了WorldRFT框架，通过分层规划分解和局部感知细化机制优化场景表示。该方法结合强化学习微调策略，在保持感知鲁棒性的同时显著提升了端到端自动驾驶的安全性和决策性能。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>58. Pseudo-Expert Regularized Offline RL for End-to-End Autonomous Driving in Photorealistic Closed-Loop Environments</strong><br><span>Chihiro Noguchi, Takaki Yamamoto</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2025-12-21</div><div>2026-04-09</div><div><a href="http://arxiv.org/abs/2512.18662v2">2512.18662v2</a> / <a href="https://arxiv.org/pdf/2512.18662v2">PDF</a></div><div>cs.RO, cs.CV</div></td>
      <td style="width: 10%; vertical-align: top;">RL</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>仅以摄像头图像作为输入并直接预测未来轨迹的端到端（E2E）自动驾驶模型，因其计算效率和通过统一优化实现泛化的潜力而备受关注；然而，由于对模仿学习（IL）的依赖，此类模型仍存在持续的失败模式。尽管在线强化学习（RL）可以缓解模仿学习带来的问题，但基于神经渲染模拟的高计算负担以及庞大的端到端网络使得迭代式奖励和超参数调整成本高昂。我们引入了一种仅使用摄像头的端到端离线强化学习框架，该框架无需额外的探索，且仅在固定的模拟器数据集上进行训练。离线强化学习具有较高的数据效率和快速的实验迭代能力，但容易受到分布外（OOD）动作高估带来的不稳定性影响。为解决此问题，我们利用专家驾驶记录构建伪基准轨迹，并将其用作行为正则化信号，在抑制不安全或次优行为模仿的同时稳定价值学习。训练和闭环评估均在从公共nuScenes数据集学习到的神经渲染环境中进行。实验结果表明，与模仿学习基准相比，所提方法在碰撞率和路线完成率方面均有显著提升。</td>
      <td style="width: 20%; vertical-align: top;">针对端到端自动驾驶模型依赖模仿学习导致的性能局限，本文提出了一种基于伪专家正则化的离线强化学习框架。该方法通过利用专家轨迹进行行为正则化以缓解分布外动作的高估问题，在无需在线探索的情况下，显著提升了模型在神经渲染闭环环境中的驾驶安全性和任务完成率。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>59. LLaViDA: A Large Language Vision Driving Assistant for Explicit Reasoning and Enhanced Trajectory Planning</strong><br><span>Yudong Liu, Spencer Hallyburton, Jiwoo Kim, Yueqian Lin, Yiming Li, Qinsi Wang, Hui Ye, Jingwei Sun, Miroslav Pajic, Yiran Chen, Hai Li</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2025-12-20</div><div>2025-12-20</div><div><a href="http://arxiv.org/abs/2512.18211v1">2512.18211v1</a> / <a href="https://arxiv.org/pdf/2512.18211v1">PDF</a></div><div>cs.RO, cs.AI</div></td>
      <td style="width: 10%; vertical-align: top;">VLM</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>轨迹规划是自动驾驶中一个基础但具有挑战性的组成部分。端到端规划器在恶劣天气、不可预测的人类行为或复杂的道路布局下经常失效，这主要是因为它们缺乏超出训练数据的强大泛化能力或少样本学习能力。我们提出了 LLaViDA，这是一种大型语言视觉驾驶助手，它利用视觉语言模型（VLM）进行物体运动预测、语义接地，并利用思维链推理进行自动驾驶中的轨迹规划。两阶段训练流程——监督微调随后进行轨迹偏好优化（TPO）——通过注入基于回归的监督来增强场景理解和轨迹规划，从而产生了一个强大的“用于自动驾驶的 VLM 轨迹规划器”。在 NuScenes 基准测试中，LLaViDA 在开环轨迹规划任务中超越了最先进的端到端及其他近期基于 VLM/LLM 的基准模型，在 NuScenes 测试集上实现了 0.31 米的平均 L2 轨迹误差和 0.10% 的碰撞率。本文代码已在 GitHub 上提供。</td>
      <td style="width: 20%; vertical-align: top;">针对端到端自动驾驶规划器在复杂场景下泛化能力不足的问题，本文提出了 LLaViDA 模型。该方法通过结合视觉语言模型、思维链推理及两阶段训练优化，显著提升了场景理解与轨迹规划性能，在 NuScenes 基准测试中表现优于现有主流方法。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>60. Vision-Language-Action Models for Autonomous Driving: Past, Present, and Future</strong><br><span>Tianshuai Hu, Xiaolu Liu, Song Wang, Yiyao Zhu, Ao Liang, Lingdong Kong, Guoyang Zhao, Zeying Gong, Jun Cen, Zhiyu Huang, Xiaoshuai Hao, Linfeng Li, Hang Song, Xiangtai Li, Jun Ma, Shaojie Shen, Jianke Zhu, Dacheng Tao, Ziwei Liu, Junwei Liang</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2025-12-18</div><div>2026-01-04</div><div><a href="http://arxiv.org/abs/2512.16760v2">2512.16760v2</a> / <a href="https://arxiv.org/pdf/2512.16760v2">PDF</a></div><div>cs.RO</div></td>
      <td style="width: 10%; vertical-align: top;">VLM</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>自动驾驶长期以来一直依赖于模块化的“感知-决策-行动”流程，其中手工设计的接口和基于规则的组件在复杂或长尾场景下经常失效。这种级联设计还会进一步传播感知误差，降低下游规划和控制的性能。视觉-行动（VA）模型通过学习从视觉输入到动作的直接映射解决了一些限制，但它们仍然不够透明，对分布偏移敏感，且缺乏结构化推理或遵循指令的能力。大型语言模型（LLM）和多模态学习的最新进展推动了视觉-语言-行动（VLA）框架的出现，这些框架将感知与基于语言的决策相结合。通过统一视觉理解、语言推理和可操作的输出，VLA 为实现更具可解释性、泛化能力和符合人类意图的驾驶策略提供了路径。本文对自动驾驶领域新兴的 VLA 图景进行了结构化描述。我们追踪了从早期 VA 方法到现代 VLA 框架的演变，并将现有方法归纳为两个主要范式：将感知、推理和规划集成在单个模型中的端到端 VLA，以及将慢速审议（通过 VLM）与快速、安全关键型执行（通过规划器）分离的双系统 VLA。在这些范式中，我们进一步区分了诸如文本与数值动作生成器以及显式与隐式引导机制等子类。我们还总结了用于评估基于 VLA 的驾驶系统的代表性数据集和基准，并重点阐述了鲁棒性、可解释性和指令忠实度等关键挑战与开放方向。总体而言，本工作旨在为推进与人类兼容的自动驾驶系统建立连贯的基础。</td>
      <td style="width: 20%; vertical-align: top;">本文综述了自动驾驶中视觉-语言-行动（VLA）模型的演进与现状，提出了端到端和双系统两种核心技术范式。文章系统分类了现有方法，探讨了关键的评估基准，并指出了该领域在鲁棒性和可解释性等方面面临的主要挑战与未来发展方向。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>61. OmniDrive-R1: Reinforcement-driven Interleaved Multi-modal Chain-of-Thought for Trustworthy Vision-Language Autonomous Driving</strong><br><span>Zhenguo Zhang, Haohan Zheng, Yishen Wang, Le Xu, Tianchen Deng, Xuefeng Chen, Qu Chen, Bo Zhang, Wuxiong Huang</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2025-12-16</div><div>2026-04-30</div><div><a href="http://arxiv.org/abs/2512.14044v3">2512.14044v3</a> / <a href="https://arxiv.org/pdf/2512.14044v3">PDF</a></div><div>cs.CV, cs.AI</div></td>
      <td style="width: 10%; vertical-align: top;">VLM, RL</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>视觉语言模型（VLMs）在自动驾驶（AD）等安全关键领域的部署受到了可靠性故障的严重阻碍，其中最显著的是物体幻觉问题。这种故障源于模型对基于文本的、缺乏视觉基础（ungrounded）的思维链（CoT）推理的依赖。虽然现有的多模态思维链方法试图缓解这一问题，但它们存在两个根本缺陷：（1）感知和推理阶段分离，导致无法进行端到端的联合优化；（2）依赖昂贵的密集定位标签。因此，我们引入了 OmniDrive-R1，这是一个专为自动驾驶设计的端到端 VLM 框架，通过交错式多模态思维链（iMCoT）机制统一了感知与推理。我们的核心创新在于强化驱动的视觉基础能力，使模型能够自主引导注意力并“放大”关键区域进行细粒度分析。这一能力通过我们纯粹的两阶段强化学习训练流程和 Clip-GRPO 算法实现。至关重要的是，Clip-GRPO 引入了一种无需标注的、基于过程的视觉基础奖励机制。该奖励不仅消除了对密集标签的需求，还通过强制执行视觉焦点与文本推理之间的实时跨模态一致性，规避了外部工具调用的不稳定性。在 DriveLMM-o1 上的大量实验证明了我们模型的显著提升。与基准模型 Qwen2.5VL-7B 相比，OmniDrive-R1 的整体推理得分从 51.77% 提升至 80.35%，最终答案准确率从 37.81% 提升至 73.62%。</td>
      <td style="width: 20%; vertical-align: top;">为解决自动驾驶中视觉语言模型推理不可靠和依赖密集标注的问题，该研究提出了 OmniDrive-R1 框架。该框架利用交错式多模态思维链和基于 Clip-GRPO 的强化学习算法，实现了无需额外标注的端到端视觉基础推理。实验证明，该方法显著提升了模型在自动驾驶场景下的推理能力与决策准确性。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>62. Tackling Snow-Induced Challenges: Safe Autonomous Lane-Keeping with Robust Reinforcement Learning</strong><br><span>Amin Jalal Aghdasian, Farzaneh Abdollahi, Ali Kamali Iglie</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2025-12-15</div><div>2025-12-15</div><div><a href="http://arxiv.org/abs/2512.12987v1">2512.12987v1</a> / <a href="https://arxiv.org/pdf/2512.12987v1">PDF</a></div><div>cs.RO, cs.AI, cs.CV, cs.LG</div></td>
      <td style="width: 10%; vertical-align: top;">RL</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>本文针对自动驾驶汽车在雪天道路环境下运行，提出了两种车道保持系统（LKS）的新算法。这些算法利用深度强化学习（DRL）来处理不确定性和打滑问题，包括动作鲁棒递归深度确定性策略梯度（AR-RDPG）和端到端动作鲁棒卷积神经网络注意力确定性策略梯度（AR-CADPG）两种决策方法。在AR-RDPG方法中，感知层首先利用多尺度神经网络对相机图像进行去噪，随后通过预训练的深度卷积神经网络（DCNN）提取中心线系数，并将这些系数与驾驶特性结合后输入到控制层。AR-CADPG方法则提出了一种端到端方案，将卷积神经网络（CNN）和注意力机制集成在DRL框架内。两种方法均在CARLA模拟器中进行训练，并在多种雪天场景下进行了验证。基于Jetson Nano的自动驾驶汽车实地实验证实了所学策略的可行性和稳定性。在两个模型中，AR-CADPG方法表现出更优的路径跟踪精度和鲁棒性，突显了在自动驾驶汽车中结合时间记忆、对抗防御和注意力机制的有效性。</td>
      <td style="width: 20%; vertical-align: top;">本文针对自动驾驶在雪天环境下车道保持的挑战，提出了AR-RDPG和AR-CADPG两种基于深度强化学习的动作鲁棒决策算法。通过引入图像去噪、特征提取及注意力机制，显著提升了车辆在复杂雪天条件下的路径跟踪精度与鲁棒性，并经仿真与实车实验验证了其有效性。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>63. From Human Intention to Action Prediction: Intention-Driven End-to-End Autonomous Driving</strong><br><span>Huan Zheng, Yucheng Zhou, Tianyi Yan, Jiayi Su, Hongjun Chen, Dubing Chen, Xingtai Gui, Wencheng Han, Runzhou Tao, Zhongying Qiu, Jianfei Yang, Jianbing Shen</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2025-12-13</div><div>2026-01-07</div><div><a href="http://arxiv.org/abs/2512.12302v2">2512.12302v2</a> / <a href="https://arxiv.org/pdf/2512.12302v2">PDF</a></div><div>cs.CV, cs.CL, cs.RO</div></td>
      <td style="width: 10%; vertical-align: top;">world model</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>尽管端到端自动驾驶在几何控制方面取得了显著进展，但目前的系统仍受限于依赖简单导航指令的命令遵循范式。要转向真正智能的代理，需要具备解释和实现高层、抽象人类意图的能力。然而，这一进步受到缺乏专用基准和语义感知评估指标的阻碍。在本文中，我们正式定义了“意图驱动的端到端自动驾驶”任务，并提出了旨在弥补这一差距的综合基准 Intention-Drive。我们构建了一个大规模数据集，其中包含复杂的自然语言意图以及高保真传感器数据。为了克服传统基于轨迹指标的局限性，我们引入了“想象未来对齐”（IFA），这是一种利用生成式世界模型评估人类目标语义实现情况的新型评估协议，而不仅仅是评估几何准确性。此外，我们通过提出两种不同的范式来探索解决方案空间：端到端视觉语言规划器和基于层次化代理的框架。实验揭示了一个关键的二分法，即现有模型表现出令人满意的驾驶稳定性，但在意图实现方面却十分吃力。值得注意的是，所提出的框架在与人类意图的对齐方面表现出优越性。</td>
      <td style="width: 20%; vertical-align: top;">针对自动驾驶系统缺乏理解高层人类意图能力的问题，本文提出了“意图驱动的端到端自动驾驶”任务及配套基准 Intention-Drive，并引入了基于生成式世界模型的语义评估协议。研究通过提出两种创新架构，弥补了现有模型在语义意图理解上的不足，有效提升了自动驾驶系统对人类意图的实现能力。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>64. Semantic-Drive: Democratizing Long-Tail Data Curation via Open-Vocabulary Grounding and Neuro-Symbolic VLM Consensus</strong><br><span>Antonio Guillen-Perez</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2025-12-12</div><div>2025-12-16</div><div><a href="http://arxiv.org/abs/2512.12012v2">2512.12012v2</a> / <a href="https://arxiv.org/pdf/2512.12012v2">PDF</a></div><div>cs.CV, cs.AI, cs.CL, cs.RO</div></td>
      <td style="width: 10%; vertical-align: top;">VLM</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>稳健自动驾驶（AV）的发展受限于“长尾”训练数据的匮乏。尽管车队收集了海量的视频日志，但识别罕见的安全关键事件（如不规则横穿马路、道路施工导向）仍然是一个人工且成本高昂的过程。现有的解决方案要么依赖缺乏精度的粗略元数据搜索，要么依赖侵犯隐私且昂贵的云端视觉语言模型（VLM）。我们推出了 Semantic-Drive，这是一个用于语义数据挖掘的本地优先、神经符号框架。我们的方法将感知过程解耦为两个阶段：（1）通过实时开放词汇检测器（YOLOE）进行符号化定位，以锁定注意力；（2）通过推理型 VLM 进行认知分析，以执行法医级的场景解析。为了减轻幻觉，我们实施了一种“系统 2”推理时对齐策略，并采用了多模型“评判-侦察”（Judge-Scout）共识机制。在 nuScenes 数据集上针对 Waymo 开放数据集（WOD-E2E）分类法进行的基准测试显示，Semantic-Drive 的召回率达到 0.966（CLIP 为 0.475），且风险评估误差比最佳单一侦察模型降低了 40%。该系统完全运行在消费级硬件（NVIDIA RTX 3090）上，提供了一种保护隐私的云端替代方案。</td>
      <td style="width: 20%; vertical-align: top;">针对自动驾驶长尾数据挖掘成本高且隐私敏感的问题，Semantic-Drive 提出了一种基于神经符号框架的本地化处理方法。该方法结合开放词汇检测与多模型共识机制，显著提升了罕见场景的识别召回率并降低了风险评估误差。系统实现了在消费级硬件上的高效运行，为大规模数据筛选提供了一种低成本且保护隐私的解决方案。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>65. FutureX: Enhance End-to-End Autonomous Driving via Latent Chain-of-Thought World Model</strong><br><span>Hongbin Lin, Yiming Yang, Yifan Zhang, Chaoda Zheng, Jie Feng, Sheng Wang, Zhennan Wang, Shijia Chen, Boyang Wang, Yu Zhang, Xianming Liu, Shuguang Cui, Zhen Li</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2025-12-12</div><div>2025-12-12</div><div><a href="http://arxiv.org/abs/2512.11226v1">2512.11226v1</a> / <a href="https://arxiv.org/pdf/2512.11226v1">PDF</a></div><div>cs.CV</div></td>
      <td style="width: 10%; vertical-align: top;">world model</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>在自动驾驶中，端到端规划器通过原始传感器数据学习场景表示，并据此生成运动规划或控制动作。然而，完全依赖当前场景进行运动规划在高度动态的交通环境中可能会导致次优响应，因为车辆自身的动作会进一步改变未来的场景。为了模拟未来场景的演变，我们利用世界模型来表示车辆与其环境如何随时间相互作用和变化，这需要复杂的推理。思维链（CoT）通过预测一系列未来思维来指导轨迹细化，提供了一种有前景的解决方案。在本文中，我们提出了 FutureX，这是一个由思维链驱动的流水线，通过未来场景潜在推理和轨迹细化来增强端到端规划器的复杂运动规划能力。具体而言，“自动思考开关”会检查当前场景并决定是否需要额外的推理来生成更高质量的运动规划。一旦 FutureX 进入“思考模式”，潜在世界模型会进行由思维链引导的推演以预测未来场景表示，从而使总结模块能够进一步细化运动规划。否则，FutureX 将以“即时模式”运行，针对相对简单的场景通过前向传播生成运动规划。大量实验表明，FutureX 在不牺牲效率的前提下，通过生成更合理的运动规划并减少碰撞，增强了现有方法，从而实现了显著的整体性能提升，例如在 NAVSIM 上将 TransFuser 的性能提升了 6.2 个 PDMS。代码将开源。</td>
      <td style="width: 20%; vertical-align: top;">针对端到端自动驾驶在复杂场景下规划效果不佳的问题，本文提出了 FutureX 框架，通过引入思维链驱动的潜在世界模型实现未来场景推理与轨迹细化。该方法利用自动思考开关在即时和思考模式间动态切换，在保证运行效率的同时，显著提升了运动规划的合理性并降低了碰撞率。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>66. SpaceDrive: Infusing Spatial Awareness into VLM-based Autonomous Driving</strong><br><span>Peizheng Li, Zhenghao Zhang, David Holtz, Hang Yu, Yutong Yang, Yuzhi Lai, Rui Song, Andreas Geiger, Andreas Zell</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2025-12-11</div><div>2025-12-11</div><div><a href="http://arxiv.org/abs/2512.10719v1">2512.10719v1</a> / <a href="https://arxiv.org/pdf/2512.10719v1">PDF</a></div><div>cs.CV</div></td>
      <td style="width: 10%; vertical-align: top;">VLM</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>基于视觉语言模型（VLM）的端到端自动驾驶方法，凭借大规模预训练所获得的通用视觉理解和强大的推理能力，经历了快速发展。然而，我们发现当前的 VLM 在理解细粒度 3D 空间关系方面存在困难，而这对与物理世界交互的系统来说是一项基本要求。为了解决这个问题，我们提出了 SpaceDrive，这是一个空间感知型 VLM 驾驶框架，它将空间信息视为显式位置编码（PE）而非文本数字标记，从而实现对语义和空间表征的联合推理。SpaceDrive 采用统一的位置编码器，对源自多视图深度估计、历史自车状态和文本提示的所有 3D 坐标进行编码。这些 3D 位置编码首先与相应的 2D 视觉标记叠加以进行增强。同时，它们作为任务无关的坐标表征，取代数字式数值标记，作为 VLM 的输入和输出。这种机制使模型能够在空间推理中更好地索引特定的视觉语义，并直接回归轨迹坐标而非逐位生成数字，从而提高了规划精度。大量实验证明，SpaceDrive 在 nuScenes 数据集上实现了最先进的开环性能，并在 Bench2Drive 闭环基准测试中以 78.02 的驾驶得分位列现有基于 VLM 方法的第二名。</td>
      <td style="width: 20%; vertical-align: top;">针对现有 VLM 在自动驾驶中缺乏细粒度 3D 空间理解能力的问题，该论文提出了 SpaceDrive 框架。该方法通过引入显式 3D 位置编码来增强视觉特征并优化坐标输入输出，实现了对语义和空间信息的联合推理。实验表明，SpaceDrive 在多个自动驾驶基准测试中显著提升了规划精度和整体驾驶性能。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>67. Closing the Navigation Compliance Gap in End-to-end Autonomous Driving</strong><br><span>Hanfeng Wu, Marlon Steiner, Michael Schmidt, Alvaro Marcos-Ramiro, Christoph Stiller</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2025-12-11</div><div>2026-03-26</div><div><a href="http://arxiv.org/abs/2512.10660v2">2512.10660v2</a> / <a href="https://arxiv.org/pdf/2512.10660v2">PDF</a></div><div>cs.CV</div></td>
      <td style="width: 10%; vertical-align: top;">distillation</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>轨迹评分规划器在遵循专家原始指令时具有较高的导航合规性，但在路口面对替代指令时表现不佳，超过30%的此类指令被忽略。我们将这种导航合规性差距归因于两个根本原因：（1）现有的指标（如Ego Progress）未能明确衡量导航依从性，从而淡化了路线内与路线外轨迹之间的差距；（2）当前数据集为每个场景仅配对一个指令，阻碍了模型学习指令依赖行为。我们通过引入二元导航合规性指标（NAVI）和派生的可控性度量（CM）来解决指标差距，并利用包含14,918个路口场景及所有可行替代指令和路由标注的NavControl数据集解决数据差距，从而产生了超过34,000个方向样本。在此基础上，我们提出了NaviHydra，这是一种融合了NAVI蒸馏和基于鸟瞰图（BEV）轨迹聚合的轨迹评分规划器，用于上下文位置感知的轨迹特征提取。NaviHydra在NAVSIM navtest拆分上获得了92.7的PDM分数，在NavControl测试拆分上获得了77.5的CM分数。使用NavControl进行训练改善了各种架构的可控性，证实了它是提升导航合规性的有效增强手段。</td>
      <td style="width: 20%; vertical-align: top;">针对端到端自动驾驶在路口执行替代指令时合规性不足的问题，本文通过引入新的合规性评价指标NAVI和大规模增强数据集NavControl，弥补了评估标准与训练数据的缺失。提出的NaviHydra模型结合了指标蒸馏与BEV特征提取，显著提升了模型在复杂路口场景下的导航指令遵循能力。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>68. Latent Chain-of-Thought World Modeling for End-to-End Driving</strong><br><span>Shuhan Tan, Kashyap Chitta, Yuxiao Chen, Ran Tian, Yurong You, Yan Wang, Wenjie Luo, Yulong Cao, Philipp Krahenbuhl, Marco Pavone, Boris Ivanovic</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2025-12-11</div><div>2026-04-14</div><div><a href="http://arxiv.org/abs/2512.10226v2">2512.10226v2</a> / <a href="https://arxiv.org/pdf/2512.10226v2">PDF</a></div><div>cs.CV, cs.RO</div></td>
      <td style="width: 10%; vertical-align: top;">world model, RL</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>近期用于自动驾驶的视觉-语言-动作（VLA）模型正在探索推理时推理，以期提升复杂场景下的驾驶性能与安全性。以往多数研究在生成驾驶动作前使用自然语言来表达思维链（CoT）推理，但文本可能并非最高效的推理表示形式。本文提出了 Latent-CoT-Drive（LCDrive）：一种在潜在语言中表达思维链的模型，该语言能够捕捉所考虑驾驶动作的可能结果。我们的方法通过在动作对齐的潜在空间中表示思维链推理与决策，将两者统一起来。模型不使用自然语言，而是交替使用以下两类标记进行推理：一是与模型输出动作共享词表的动作提议标记，二是基于学习到的潜在世界模型并表达动作未来结果的世界模型标记。我们通过基于场景真实未来推演监督模型的动作提议和世界模型标记，对潜在思维链进行冷启动，随后通过闭环强化学习进行后训练以增强推理能力。在一个大规模端到端驾驶基准测试中，与非推理及文本推理基线相比，LCDrive 实现了更快的推理速度、更好的轨迹质量，并从交互式强化学习中获得了更大的性能提升。</td>
      <td style="width: 20%; vertical-align: top;">本文针对自动驾驶推理效率问题，提出了一种名为 LCDrive 的模型，通过在潜在空间中交替使用动作提议和世界模型标记来执行思维链推理。该方法将推理与决策统一在动作对齐的潜在空间中，并通过闭环强化学习进一步优化。实验表明，该模型在端到端驾驶任务中显著提升了推理速度和轨迹质量。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>69. UniUGP: Unifying Understanding, Generation, and Planing For End-to-end Autonomous Driving</strong><br><span>Hao Lu, Ziyang Liu, Guangfeng Jiang, Yuanfei Luo, Sheng Chen, Yangang Zhang, Ying-Cong Chen</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2025-12-10</div><div>2025-12-10</div><div><a href="http://arxiv.org/abs/2512.09864v1">2512.09864v1</a> / <a href="https://arxiv.org/pdf/2512.09864v1">PDF</a></div><div>cs.CV</div></td>
      <td style="width: 10%; vertical-align: top;">VLM, world model</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>由于世界知识有限和视觉动态建模能力较弱，自动驾驶（AD）系统在长尾场景中表现不佳。现有的基于视觉-语言-动作（VLA）的方法无法利用未标记视频进行视觉因果学习，而基于世界模型的方法则缺乏大语言模型的推理能力。在本文中，我们构建了多个专门的数据集，为复杂场景提供推理和规划标注。随后，我们提出了一个名为 UniUGP 的统一理解-生成-规划框架，通过混合专家架构协同场景推理、未来视频生成和轨迹规划。通过集成预训练的视觉语言模型（VLM）和视频生成模型，UniUGP 利用视觉动态和语义推理来增强规划性能。该模型以多帧观测和语言指令作为输入，能够输出可解释的思维链推理、物理一致的轨迹以及连贯的未来视频。我们引入了一种四阶段训练策略，在多个现有自动驾驶数据集及所提出的专业数据集上逐步构建这些能力。实验表明，该方法在感知、推理和决策方面达到了最先进的性能，并在应对具有挑战性的长尾情况时展现出优越的泛化能力。</td>
      <td style="width: 20%; vertical-align: top;">针对自动驾驶在长尾场景中推理与规划能力不足的问题，本文提出了 UniUGP 框架，通过集成视觉语言模型与视频生成模型，实现了场景理解、未来预测与轨迹规划的统一。该模型通过混合专家架构与多阶段训练策略，在提升感知和决策性能的同时，展现了出色的长尾场景泛化能力。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>70. COVLM-RL: Critical Object-Oriented Reasoning for Autonomous Driving Using VLM-Guided Reinforcement Learning</strong><br><span>Lin Li, Yuxin Cai, Jianwu Fang, Jianru Xue, Chen Lv</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2025-12-10</div><div>2025-12-10</div><div><a href="http://arxiv.org/abs/2512.09349v1">2512.09349v1</a> / <a href="https://arxiv.org/pdf/2512.09349v1">PDF</a></div><div>cs.RO</div></td>
      <td style="width: 10%; vertical-align: top;">VLM, RL</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>端到端自动驾驶框架在泛化能力、训练效率和可解释性方面持续面临挑战。虽然近期方法利用视觉语言模型（VLM）在大型数据集上进行监督学习以提高推理能力，但它们在面对新场景时往往缺乏鲁棒性。相反，基于强化学习（RL）的方法虽然增强了适应性，但存在数据效率低下且缺乏透明决策的问题。为了解决这些局限性，我们提出了 COVLM-RL，这是一种将关键面向对象（CO）推理与 VLM 引导的强化学习相结合的全新端到端驾驶框架。具体而言，我们设计了一种思维链（CoT）提示策略，使 VLM 能够对关键交通要素进行推理并生成高层语义决策，从而有效地将多视角视觉输入转化为结构化的语义决策先验。这些先验降低了输入维度，并将任务相关知识注入到强化学习循环中，从而加速了训练并提高了策略的可解释性。然而，将高层语义引导与连续的底层控制相结合仍然并非易事。为此，我们引入了一种一致性损失函数，旨在促进 VLM 的语义规划与强化学习智能体的控制输出之间的一致性，进而增强了可解释性和训练稳定性。在 CARLA 仿真器中进行的实验表明，COVLM-RL 在训练过的驾驶环境中将成功率提高了 30%，在未见过的环境中提高了 50%，凸显了其强大的泛化能力。</td>
      <td style="width: 20%; vertical-align: top;">针对端到端自动驾驶在泛化性和可解释性上的不足，本文提出了 COVLM-RL 框架。该方法通过思维链引导 VLM 生成语义决策先验，并结合一致性损失将高层推理与强化学习控制相结合。实验证明，该方法显著提升了模型在已知及未知环境下的驾驶成功率与泛化能力。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>71. DiffusionDriveV2: Reinforcement Learning-Constrained Truncated Diffusion Modeling in End-to-End Autonomous Driving</strong><br><span>Jialv Zou, Shaoyu Chen, Bencheng Liao, Zhiyu Zheng, Yuehao Song, Lefei Zhang, Qian Zhang, Wenyu Liu, Xinggang Wang</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2025-12-08</div><div>2025-12-08</div><div><a href="http://arxiv.org/abs/2512.07745v1">2512.07745v1</a> / <a href="https://arxiv.org/pdf/2512.07745v1">PDF</a></div><div>cs.CV</div></td>
      <td style="width: 10%; vertical-align: top;">RL</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>端到端自动驾驶的生成式扩散模型往往面临模式坍塌的问题，倾向于生成保守且同质化的行为。尽管DiffusionDrive利用代表不同驾驶意图的预定义锚点来划分动作空间并生成多样的轨迹，但其对模仿学习的依赖缺乏足够的约束，导致在多样性和高质量一致性之间陷入两难。在本文中，我们提出了DiffusionDriveV2，利用强化学习来约束低质量模式并探索更优的轨迹。这在保留其核心高斯混合模型固有模态的同时，显著提升了整体输出质量。首先，我们使用适合轨迹规划的尺度自适应乘法噪声来促进广泛探索。其次，我们采用锚点内GRPO（组相对策略优化）来管理单一锚点生成样本间的优势估计，并使用锚点间截断GRPO来整合跨锚点的全局视角，从而防止不同意图（如转弯与直行）之间不恰当的优势比较，这有助于避免进一步的模式坍塌。DiffusionDriveV2在NAVSIM v1数据集上达到了91.2的PDMS，在NAVSIM v2数据集上达到了85.5的EPDMS（闭环评估，基于对齐的ResNet-34主干），创下了新纪录。进一步的实验验证了我们的方法解决了截断扩散模型在多样性和高质量一致性之间的两难困境，实现了最佳平衡。代码和模型将在https://github.com/hustvl/DiffusionDriveV2发布。</td>
      <td style="width: 20%; vertical-align: top;">针对端到端自动驾驶中扩散模型生成行为单一且质量不稳定的问题，本文提出了DiffusionDriveV2模型。通过引入尺度自适应噪声以及锚点内外的GRPO强化学习机制，该方法在保证轨迹多样性的同时有效提升了质量，在NAVSIM数据集的闭环评估中取得了领先表现。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>72. TrajMoE: Scene-Adaptive Trajectory Planning with Mixture of Experts and Reinforcement Learning</strong><br><span>Zebin Xing, Pengxuan Yang, Linbo Wang, Yichen Zhang, Yiming Hu, Yupeng Zheng, Junli Wang, Yinfeng Gao, Guang Li, Kun Ma, Long Chen, Zhongpu Xia, Qichao Zhang, Hangjun Ye, Dongbin Zhao</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2025-12-08</div><div>2025-12-09</div><div><a href="http://arxiv.org/abs/2512.07135v2">2512.07135v2</a> / <a href="https://arxiv.org/pdf/2512.07135v2">PDF</a></div><div>cs.CV, cs.AI</div></td>
      <td style="width: 10%; vertical-align: top;">RL</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>目前的自动驾驶系统通常偏好端到端框架，即利用神经网络将图像等传感器输入映射到轨迹空间。既往研究表明，当模型具备可能的轨迹先验分布时，可以实现更好的规划性能。然而，这些方法通常忽视了两个关键方面：1）合适的轨迹先验在不同的驾驶场景中差异巨大；2）其轨迹评估机制缺乏由策略驱动的优化，仍受限于单阶段监督训练的局限性。为解决这些问题，我们探索了两个关键领域的改进。针对问题1，我们采用专家混合（MoE）技术，针对不同场景应用量身定制的轨迹先验。针对问题2，我们利用强化学习对轨迹评分机制进行微调。此外，我们整合了具有不同感知骨干网的模型以增强感知特征。我们的集成模型在navsim ICCV基准测试中取得了51.08分，位列第三。</td>
      <td style="width: 20%; vertical-align: top;">针对自动驾驶中场景通用性差和轨迹评估受限于监督学习的问题，本文提出了TrajMoE框架。该方法利用专家混合模型实现场景自适应的轨迹先验，并通过强化学习对轨迹评分机制进行优化。实验结果显示，该方法在navsim ICCV基准测试中表现优异，提升了规划的准确性和鲁棒性。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>73. Spatial Retrieval Augmented Autonomous Driving</strong><br><span>Xiaosong Jia, Chenhe Zhang, Yule Jiang, Songbur Wong, Zhiyuan Zhang, Chen Chen, Shaofeng Zhang, Xuanhe Zhou, Xue Yang, Junchi Yan, Yu-Gang Jiang</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2025-12-07</div><div>2025-12-07</div><div><a href="http://arxiv.org/abs/2512.06865v1">2512.06865v1</a> / <a href="https://arxiv.org/pdf/2512.06865v1">PDF</a></div><div>cs.CV</div></td>
      <td style="width: 10%; vertical-align: top;"></td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>现有的自动驾驶系统依赖车载传感器（摄像头、激光雷达、惯性测量单元等）进行环境感知。然而，这种范式受限于驾驶过程中的感知视域，在视野受限、遮挡或黑暗、雨天等极端条件下往往表现不佳。相比之下，人类驾驶员即便在能见度较差的情况下也能回想道路结构。为了赋予模型这种“回想”能力，我们提出了空间检索范式，引入离线检索的地理图像作为额外输入。这些图像无需额外传感器即可从离线缓存（如谷歌地图或已存储的自动驾驶数据集）中轻松获取，使其成为现有自动驾驶任务的即插即用扩展。在实验方面，我们首先利用谷歌地图API检索的地理图像扩展了nuScenes数据集，并将新数据与自车轨迹对齐。我们建立了五个核心自动驾驶任务的基准：目标检测、在线地图绘制、占用预测、端到端规划以及生成式世界建模。广泛的实验表明，这种扩展模态可以提升某些任务的性能。我们将开源数据集整理代码、数据和基准，以供对这一新型自动驾驶范式的进一步研究。</td>
      <td style="width: 20%; vertical-align: top;">针对自动驾驶系统在受限环境或极端条件下感知能力不足的问题，本文提出了一种空间检索范式，通过引入离线地理图像作为补充输入来提升模型表现。该方法作为即插即用的扩展，在目标检测、规划和世界建模等多个核心任务中均展现出性能改进，并提供了相应的基准数据集。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>74. WAM-Diff: A Masked Diffusion VLA Framework with MoE and Online Reinforcement Learning for Autonomous Driving</strong><br><span>Mingwang Xu, Jiahao Cui, Feipeng Cai, Hanlin Shang, Zhihao Zhu, Shan Luan, Yifang Xu, Neng Zhang, Yaoyi Li, Jia Cai, Siyu Zhu</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2025-12-06</div><div>2025-12-06</div><div><a href="http://arxiv.org/abs/2512.11872v1">2512.11872v1</a> / <a href="https://arxiv.org/pdf/2512.11872v1">PDF</a></div><div>cs.RO, cs.AI, cs.CV</div></td>
      <td style="width: 10%; vertical-align: top;">RL</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>基于视觉-语言-动作（VLA）模型的端到端自动驾驶系统集成了多模态传感器输入和语言指令，以生成规划与控制信号。尽管自回归大语言模型和连续扩散策略已较为普遍，但离散掩码扩散在轨迹生成中的潜力仍未得到充分探索。本文提出了 WAM-Diff，这是一种采用掩码扩散迭代优化表示未来自车轨迹的离散序列的 VLA 框架。我们的方法具有三个关键创新：一是系统性地调整了适用于自动驾驶的掩码扩散，支持灵活的非因果解码顺序；二是通过稀疏专家混合（MoE）架构实现了可扩展的模型容量，并在运动预测和面向驾驶的视觉问答（VQA）任务上进行联合训练；三是使用组序列策略优化（GSPO）进行在线强化学习，以优化序列级的驾驶奖励。值得注意的是，我们的模型在 NAVSIM-v1 上达到了 91.0 的 PDMS，在 NAVSIM-v2 上达到了 89.7 的 EPDMS，证明了掩码扩散在自动驾驶中的有效性。该方法为自回归和基于扩散的策略提供了一种有前景的替代方案，支持场景感知的轨迹生成解码策略。</td>
      <td style="width: 20%; vertical-align: top;">针对自动驾驶轨迹生成问题，本文提出了 WAM-Diff 框架，通过引入掩码扩散模型、稀疏 MoE 架构以及基于 GSPO 的在线强化学习来优化轨迹预测。该方法在 NAVSIM 基准测试中表现优异，为端到端自动驾驶系统提供了一种高效的非自回归生成策略。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>75. BeLLA: End-to-End Birds Eye View Large Language Assistant for Autonomous Driving</strong><br><span>Karthik Mohan, Sonam Singh, Amit Arvind Kale</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2025-12-05</div><div>2025-12-05</div><div><a href="http://arxiv.org/abs/2512.06096v1">2512.06096v1</a> / <a href="https://arxiv.org/pdf/2512.06096v1">PDF</a></div><div>cs.CV</div></td>
      <td style="width: 10%; vertical-align: top;">VLM</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>视觉语言模型（VLM）和多模态语言模型（MLLM）的快速发展，通过实现更丰富的场景理解、情境感知推理和更具可解释性的决策，显著重塑了自动驾驶研究领域。然而，许多现有工作往往依赖于单视角编码器，无法利用多相机系统的空间结构，或者在缺乏统一空间表示的聚合多视图特征上运行，这使得推断以自我为中心的方位、物体关系和更广泛的背景变得更加困难。因此，我们提出了 BeLLA，这是一种将统一的 360° BEV 表示与大语言模型连接起来的端到端架构，用于自动驾驶中的问答。我们主要使用 NuScenes-QA 和 DriveLM 两个基准测试来评估我们的工作，结果显示 BeLLA 在需要更强空间推理的问题（如涉及物体相对位置和附近物体行为理解的问题）上持续优于现有方法，在某些任务上实现了高达 +9.3% 的绝对性能提升。在其他类别中，BeLLA 的表现也具有竞争力，证明了其处理多样化问题的能力。</td>
      <td style="width: 20%; vertical-align: top;">针对自动驾驶中多视图特征空间表示不统一、难以进行复杂空间推理的问题，本文提出了 BeLLA 架构，将 360° 鸟瞰图（BEV）与大语言模型相结合。实验结果表明，该方法在 NuScenes-QA 和 DriveLM 等基准测试中，尤其在涉及空间推理和行为理解的任务上取得了显著的性能提升。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>76. dVLM-AD: Enhance Diffusion Vision-Language-Model for Driving via Controllable Reasoning</strong><br><span>Yingzi Ma, Yulong Cao, Wenhao Ding, Shuibai Zhang, Yan Wang, Boris Ivanovic, Ming Jiang, Marco Pavone, Chaowei Xiao</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2025-12-04</div><div>2025-12-04</div><div><a href="http://arxiv.org/abs/2512.04459v1">2512.04459v1</a> / <a href="https://arxiv.org/pdf/2512.04459v1">PDF</a></div><div>cs.CV</div></td>
      <td style="width: 10%; vertical-align: top;">VLM</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>自动驾驶领域正日益关注如何应对分布外（OOD）驾驶场景所带来的挑战。一种主流的研究趋势是通过整合视觉语言模型（VLM）来增强端到端（E2E）驾驶系统，利用其丰富的世界知识和推理能力来提高在不同环境下的泛化能力。然而，大多数现有的VLM或视觉语言智能体（VLA）是基于自回归（AR）模型构建的。在本文中，我们观察到现有的基于AR的VLM受限于因果注意力和序列Token生成，往往难以在高层推理和底层规划之间保持一致性和可控性。相比之下，最近配备双向注意力的离散扩散VLM通过迭代去噪表现出了卓越的可控性和可靠性。基于这些观察，我们引入了dVLM-AD，这是一种基于扩散的视觉语言模型，将感知、结构化推理和底层规划统一用于端到端驾驶。在nuScenes和WOD-E2E上的评估表明，尽管dVLM-AD使用了较小的骨干网络，但仍能产生更一致的推理-动作对，并实现了与现有驾驶VLM/VLA系统相当的规划性能。在长尾WOD-E2E场景中，其行为轨迹一致性提高了9%，RFS提高了6%，优于基于AR的基准模型。这些结果表明了一种可控且可靠的、可扩展的端到端驾驶实现路径。</td>
      <td style="width: 20%; vertical-align: top;">针对现有基于自回归的视觉语言模型在自动驾驶任务中难以平衡推理与规划一致性的问题，本文提出了dVLM-AD模型。该方法利用扩散模型的双向注意力和迭代去噪机制，实现了感知、推理与规划的统一。实验结果表明，该模型在端到端驾驶中表现出了更高的一致性和更好的长尾场景处理能力。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>77. MindDrive: An All-in-One Framework Bridging World Models and Vision-Language Model for End-to-End Autonomous Driving</strong><br><span>Bin Sun, Yaoguang Cao, Yan Wang, Rui Wang, Jiachen Shang, Xiejie Feng, Jiayi Lu, Jia Shi, Shichun Yang, Xiaoyu Yan, Ziying Song</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2025-12-04</div><div>2025-12-08</div><div><a href="http://arxiv.org/abs/2512.04441v2">2512.04441v2</a> / <a href="https://arxiv.org/pdf/2512.04441v2">PDF</a></div><div>cs.CV</div></td>
      <td style="width: 10%; vertical-align: top;">VLM, world model</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>端到端自动驾驶（E2E-AD）已成为一种新的范式，其中轨迹规划发挥着至关重要的作用。现有研究主要遵循两个方向：面向轨迹生成的方法，侧重于通过简单的决策机制产生高质量轨迹；面向轨迹选择的方法，通过多维度评估选择最佳轨迹，但缺乏足够的生成能力。本文提出了 MindDrive，这是一个将高质量轨迹生成与全面决策推理相集成的统一框架。它建立了一个“情境模拟-候选生成-多目标权衡”的结构化推理范式。特别地，所提出的基于世界动作模型（WaM）的未来感知轨迹生成器（FaTG），执行以自我为条件的“假设”模拟，以预测潜在的未来场景并生成具有前瞻性的候选轨迹。在此基础上，面向视觉语言模型的评估器（VLoE）利用大视觉语言模型的推理能力，在安全性、舒适性和效率维度上进行多目标评估，从而实现合理且符合人类偏好的决策。在 NAVSIM-v1 和 NAVSIM-v2 基准测试上的广泛实验表明，MindDrive 在多维度驾驶指标上达到了最先进的性能，显著增强了安全性、合规性和泛化能力。这项工作为迈向可解释和认知驱动的自动驾驶提供了一条有前景的路径。</td>
      <td style="width: 20%; vertical-align: top;">针对端到端自动驾驶中轨迹生成与决策推理分离的问题，MindDrive 框架整合了基于世界模型的轨迹生成与基于视觉语言模型的推理评估。该方法通过“情境模拟-候选生成-多目标权衡”范式，有效提升了自动驾驶系统在安全性、舒适性与效率方面的表现，并增强了决策的可解释性。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>78. RoaD: Rollouts as Demonstrations for Closed-Loop Supervised Fine-Tuning of Autonomous Driving Policies</strong><br><span>Guillermo Garcia-Cobo, Maximilian Igl, Peter Karkus, Zhejun Zhang, Michael Watson, Yuxiao Chen, Boris Ivanovic, Marco Pavone</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2025-12-01</div><div>2025-12-01</div><div><a href="http://arxiv.org/abs/2512.01993v1">2512.01993v1</a> / <a href="https://arxiv.org/pdf/2512.01993v1">PDF</a></div><div>cs.RO, cs.AI, cs.CV, cs.LG</div></td>
      <td style="width: 10%; vertical-align: top;">RL</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>自动驾驶策略通常通过对人类演示进行开环行为克隆来训练。然而，此类策略在闭环部署时会遭遇协变量偏移，导致误差累积。我们引入了“回放即演示”（RoaD），这是一种简单高效的方法，通过利用策略自身的闭环回放作为额外的训练数据来缓解协变量偏移。在回放生成过程中，RoaD 结合专家指导，引导轨迹向高质量行为偏移，从而产生既具信息量又真实的演示数据用于微调。该方法能够实现稳健的闭环适配，所需数据量比强化学习少几个数量级，并避免了先前闭环监督微调（CL-SFT）方法中限制性的假设，使其能够应用于包括端到端驾驶在内的更广泛领域。我们在大规模交通模拟基准 WOSAC 上验证了 RoaD 的有效性，其表现优于或持平于之前的 CL-SFT 方法；在基于高保真神经重建的端到端驾驶模拟器 AlpaSim 中，RoaD 将驾驶评分提高了 41%，并将碰撞率降低了 54%。</td>
      <td style="width: 20%; vertical-align: top;">针对自动驾驶策略在闭环部署中因协变量偏移导致的误差累积问题，本文提出了 RoaD 方法，通过结合专家指导的闭环回放数据进行微调。该方法在无需强化学习大规模数据的前提下，有效提升了自动驾驶策略的鲁棒性和性能，在多个仿真基准中显著改善了驾驶评分并降低了碰撞率。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>79. New Spiking Architecture for Multi-Modal Decision-Making in Autonomous Vehicles</strong><br><span>Aref Ghoreishee, Abhishek Mishra, Lifeng Zhou, John Walsh, Nagarajan Kandasamy</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2025-12-01</div><div>2025-12-01</div><div><a href="http://arxiv.org/abs/2512.01882v1">2512.01882v1</a> / <a href="https://arxiv.org/pdf/2512.01882v1">PDF</a></div><div>cs.LG</div></td>
      <td style="width: 10%; vertical-align: top;">RL</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>本文提出了一种用于自动驾驶车辆高层决策的端到端多模态强化学习框架。该框架通过基于交叉注意力机制的 Transformer 感知模块，集成了包括摄像头图像、激光雷达点云和车辆航向信息在内的异构传感器输入。尽管 Transformer 已成为现代多模态架构的核心，但其高昂的计算成本限制了其在资源受限边缘环境中的部署。为克服这一挑战，我们提出了一种具有时间感知能力的脉冲 Transformer 类架构，该架构利用三值脉冲神经元实现计算高效的多模态融合。在高速公路环境的多项任务中进行的全面评估证明了该方法在实时自动驾驶决策方面的有效性和效率。</td>
      <td style="width: 20%; vertical-align: top;">针对自动驾驶中多模态感知与高层决策的计算资源限制问题，本文提出了一种基于三值脉冲神经元的时间感知 Transformer 架构。该方法实现了多模态信息的高效融合，在保证自动驾驶决策有效性的同时，显著提升了在资源受限环境下的计算效率。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>80. OpenREAD: Reinforced Open-Ended Reasoning for End-to-End Autonomous Driving with LLM-as-Critic</strong><br><span>Songyan Zhang, Wenhui Huang, Zhan Chen, Chua Jiahao Collister, Qihang Huang, Chen Lv</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2025-12-01</div><div>2025-12-02</div><div><a href="http://arxiv.org/abs/2512.01830v2">2512.01830v2</a> / <a href="https://arxiv.org/pdf/2512.01830v2">PDF</a></div><div>cs.CV</div></td>
      <td style="width: 10%; vertical-align: top;">VLM, RL</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>近期，两阶段微调策略（例如通过监督微调（SFT）获取基础驾驶知识，并进一步通过强化微调（RFT）增强决策与规划）在推进知识驱动型自动驾驶（AD）范式方面展现出巨大潜力。然而，SFT的学习本质限制了推理的泛化能力，进而制约了驾驶性能的全面发挥。同时，当前的RFT方法主要应用于下游任务，因为场景理解是一个开放式问题，其相应的奖励难以量化。为了解决这些限制，我们提出了OpenREAD，这是一种基于视觉-语言模型（VLM）的开放式推理强化自动驾驶框架，实现了从高层推理到低层轨迹规划的全流程端到端RFT。具体而言，我们首先在开源驾驶相关知识数据集上构建大规模思维链（CoT）标注，并采用强大的Qwen3大语言模型（LLM）作为RFT中的评论家，在奖励建模过程中量化开放式问题的推理质量。大量实验证实，联合端到端RFT在上下游任务中均带来了显著提升，使OpenREAD在推理和规划基准测试中达到了最先进的性能。</td>
      <td style="width: 20%; vertical-align: top;">针对自动驾驶中推理泛化能力不足及开放式场景奖励难以量化的问题，本文提出了OpenREAD框架。该研究利用大模型作为评论家进行强化微调，实现了从推理到规划的端到端优化。实验证明，该方法在驾驶推理和轨迹规划任务上均取得了业内领先的性能。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>81. RoboDriveVLM: A Novel Benchmark and Baseline towards Robust Vision-Language Models for Autonomous Driving</strong><br><span>Dacheng Liao, Mengshi Qi, Peng Shu, Zhining Zhang, Yuxin Lin, Liang Liu, Huadong Ma</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2025-12-01</div><div>2025-12-01</div><div><a href="http://arxiv.org/abs/2512.01300v1">2512.01300v1</a> / <a href="https://arxiv.org/pdf/2512.01300v1">PDF</a></div><div>cs.AI</div></td>
      <td style="width: 10%; vertical-align: top;">VLM, distillation</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>当前基于视觉语言模型（VLM）的端到端自动驾驶系统，通常利用大语言模型根据对当前场景的理解直接生成驾驶决策。然而，此类系统在现实驾驶场景中引入了多种风险。为了评估VLM是否真正适用于自动驾驶，我们推出了RoboDriveBench，这是首个专注于端到端轨迹预测任务的鲁棒性基准测试。该基准通过涵盖各种损坏类型的11个模拟场景，系统地评估了VLM端到端自动驾驶系统面临的两类关键现实挑战：包括6种由环境变化引起的传感器损坏场景，以及5种由人为干预和数据传输故障导致的提示词损坏案例。每种损坏类型包含250个独特的驾驶场景和5,689帧数据，每次评估总计产生64,559个轨迹预测案例。为了克服这些挑战，我们提出了一种名为RoboDriveVLM的新型VLM自动驾驶框架，通过将更多多模态数据（如激光雷达和雷达数据）映射到统一的潜空间来增强鲁棒性。此外，我们引入了一种基于跨模态知识蒸馏的测试时适应（TTA）方法，以提高VLM自动驾驶系统的鲁棒性。通过广泛的实验，我们的工作揭示了当前VLM端到端自动驾驶系统的局限性，并为现实部署提供了更可靠的解决方案。源代码和数据集将公开。</td>
      <td style="width: 20%; vertical-align: top;">针对基于VLM的自动驾驶系统在真实场景中的鲁棒性问题，本文提出了RoboDriveBench基准测试以评估传感器和提示词损坏带来的影响。为此，作者开发了RoboDriveVLM框架，通过引入多模态融合与测试时适应（TTA）方法，显著提升了系统的鲁棒性与可靠性。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>82. CoT4AD: A Vision-Language-Action Model with Explicit Chain-of-Thought Reasoning for Autonomous Driving</strong><br><span>Zhaohui Wang, Tengbo Yu, Hao Tang</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2025-11-27</div><div>2025-11-27</div><div><a href="http://arxiv.org/abs/2511.22532v1">2511.22532v1</a> / <a href="https://arxiv.org/pdf/2511.22532v1">PDF</a></div><div>cs.CV, cs.AI</div></td>
      <td style="width: 10%; vertical-align: top;">VLM</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>视觉-语言-动作（VLA）模型因其强大的推理能力和丰富的世界知识，近期在端到端自动驾驶领域备受关注。然而，现有的 VLA 模型往往在数值推理能力方面存在局限，且输入输出映射过于简化，这阻碍了它们在需要逐步因果推理的复杂驾驶场景中的表现。为了应对这些挑战，我们提出了 CoT4AD，这是一个新颖的 VLA 框架，旨在将思维链（CoT）推理引入自动驾驶，以增强视觉语言模型（VLM）的数值推理和因果推理能力。CoT4AD 集成了视觉观测和语言指令，用于执行语义推理、场景理解和轨迹规划。在训练期间，它显式地建模了“感知-提问-预测-动作”的思维链，以跨多个驾驶任务对齐推理空间与动作空间。在推理期间，它执行隐式思维链推理，从而在动态环境中实现一致的数值推理和稳健的决策。在 nuScenes 和 Bench2Drive 等真实世界和模拟基准测试上的大量实验表明，CoT4AD 在开环和闭环评估中均达到了最先进的性能。</td>
      <td style="width: 20%; vertical-align: top;">针对自动驾驶中现有 VLA 模型数值与因果推理能力不足的问题，本文提出了 CoT4AD 框架。该模型通过显式建模“感知-提问-预测-动作”的思维链，有效增强了复杂场景下的推理和决策能力，在多项主流自动驾驶基准测试中表现卓越。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>83. AD-R1: Closed-Loop Reinforcement Learning for End-to-End Autonomous Driving with Impartial World Models</strong><br><span>Tianyi Yan, Tao Tang, Xingtai Gui, Yongkang Li, Jiasen Zhesng, Weiyao Huang, Lingdong Kong, Wencheng Han, Xia Zhou, Xueyang Zhang, Yifei Zhan, Kun Zhan, Cheng-zhong Xu, Jianbing Shen</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2025-11-25</div><div>2026-03-11</div><div><a href="http://arxiv.org/abs/2511.20325v3">2511.20325v3</a> / <a href="https://arxiv.org/pdf/2511.20325v3">PDF</a></div><div>cs.CV</div></td>
      <td style="width: 10%; vertical-align: top;">world model, RL</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>端到端自动驾驶模型有望直接从传感器数据中学习复杂行为，但在安全性和处理长尾事件方面面临严峻挑战。强化学习（RL）为克服这些局限性提供了一条有希望的途径，但其在自动驾驶领域的成功一直难以实现。我们发现阻碍这一进展的根本缺陷在于：强化学习所使用的世界模型中存在深层的乐观偏差。为了解决这个问题，我们引入了一个围绕“公正世界模型”（Impartial World Model）构建的策略后训练优化框架。我们的主要贡献在于训练该模型诚实地预判危险。我们通过一种新颖的数据合成流水线——反事实合成（Counterfactual Synthesis）来实现这一点，该方法系统地生成了一套丰富的、合理的碰撞和偏离道路事件课程。这使得模型从被动的场景补全者转变为能够忠实于动作与结果之间因果关系的真实预测者。随后，我们将此公正世界模型集成到我们的闭环强化学习框架中，使其充当内部评估器。在优化过程中，智能体通过查询该评估器来“梦境模拟”候选动作的结果。通过包括全新风险预见基准在内的大量实验证明，我们的模型在预测失败方面显著优于基准方法。因此，当将其作为评估器使用时，它能够在具有挑战性的模拟中显著减少安全违规，证明了教导模型“预见危险”是构建真正安全且智能的自动驾驶智能体的关键一步。</td>
      <td style="width: 20%; vertical-align: top;">针对自动驾驶强化学习中世界模型的乐观偏差问题，本文提出了一种包含“公正世界模型”的闭环优化框架，通过反事实数据合成提升模型对潜在危险的预测能力。该方法通过将模型作为内部评估器指导策略学习，在模拟实验中显著降低了安全违规率，验证了提升模型危险预判能力对自动驾驶安全的重要性。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>84. Map-World: Masked Action planning and Path-Integral World Model for Autonomous Driving</strong><br><span>Bin Hu, Zijian Lu, Haicheng Liao, Chengran Yuan, Bin Rao, Yongkang Li, Guofa Li, Zhiyong Cui, Cheng-zhong Xu, Zhenning Li</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2025-11-25</div><div>2025-11-25</div><div><a href="http://arxiv.org/abs/2511.20156v1">2511.20156v1</a> / <a href="https://arxiv.org/pdf/2511.20156v1">PDF</a></div><div>cs.CV, cs.RO</div></td>
      <td style="width: 10%; vertical-align: top;">world model, RL</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>自动驾驶的运动规划必须在处理多种可能未来的同时保持计算效率。近期的端到端系统和基于世界模型的规划器虽然能预测丰富的多模态轨迹，但通常依赖手工设计的锚点或强化学习来选择单一最佳模式进行训练和控制。这种选择方式丢弃了关于替代性未来的信息，并增加了优化的复杂度。我们提出了MAP-World，这是一种无先验的多模态规划框架，将掩码动作规划与路径加权世界模型相结合。掩码动作规划（MAP）模块将未来的自车运动视为掩码序列补全问题：过去的航点被编码为可见令牌，未来航点表现为掩码令牌，且驾驶意图路径提供了粗略的框架。紧凑的潜空间规划状态通过注入噪声扩展为多个轨迹查询，从而在无需锚点库或教师策略的情况下产生多样且时间一致的模态。随后，一个轻量级的世界模型根据每个候选轨迹展开未来的鸟瞰图（BEV）语义。在训练过程中，语义损失通过模态期望计算，并使用轨迹概率作为离散路径权重，使得规划器能够从所有合理未来的完整分布中学习，而非仅从单一路径中学习。在NAVSIM数据集上，我们的方法与基于锚点的方法表现相当，并在基于世界模型的方法中达到了最先进的性能，同时避免了强化学习并保持了实时推理延迟。</td>
      <td style="width: 20%; vertical-align: top;">针对现有自动驾驶规划依赖人工锚点或强化学习导致优化复杂的问题，本文提出了MAP-World框架。该方法将未来轨迹预测建模为掩码序列补全任务，并利用路径加权世界模型进行多模态学习，从而在无需复杂策略的情况下实现了高效、多样且全局优化的路径规划。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>85. CoC-VLA: Delving into Adversarial Domain Transfer for Explainable Autonomous Driving via Chain-of-Causality Visual-Language-Action Model</strong><br><span>Dapeng Zhang, Fei Shen, Rui Zhao, Yinda Chen, Peng Zhi, Chenyang Li, Rui Zhou, Qingguo Zhou</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2025-11-25</div><div>2025-11-25</div><div><a href="http://arxiv.org/abs/2511.19914v1">2511.19914v1</a> / <a href="https://arxiv.org/pdf/2511.19914v1">PDF</a></div><div>cs.RO</div></td>
      <td style="width: 10%; vertical-align: top;">VLM</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>自动驾驶是人工智能的一个重要应用领域。近期的研究重点已从仅关注常见场景转向解决复杂的长尾问题，如微妙的人类行为、交通事故及违规驾驶模式。鉴于大型语言模型（LLMs）在理解视觉和自然语言输入以及遵循指令方面的强大能力，现有方法已将LLMs整合进自动驾驶系统，以增强其在多种场景下的推理、可解释性和性能。然而，目前的方法通常要么依赖于适用于工业部署的真实世界数据，要么依赖于针对罕见或困难场景设计的仿真数据，很少有方法能有效结合两者的互补优势。为了解决这一局限性，我们提出了一种新颖的由VLM引导的端到端对抗性迁移框架，名为CoC-VLA，旨在将仿真环境中的长尾处理能力迁移至真实世界部署。该框架由教师VLM模型、学生VLM模型和判别器组成。教师和学生VLM模型共享一种名为因果链视觉语言模型（CoC VLM）的基础架构，该架构通过端到端文本适配器整合了时间信息，并支持思维链推理以推断复杂的驾驶逻辑。教师和学生VLM模型分别在仿真数据集和真实世界数据集上进行预训练。判别器则通过一种新颖的反向传播策略进行对抗性训练，以促进学生VLM模型将处理长尾场景的能力从仿真环境迁移到真实世界环境。</td>
      <td style="width: 20%; vertical-align: top;">针对自动驾驶在复杂长尾场景下的处理难题，本文提出了一种基于因果链视觉语言模型（CoC-VLA）的对抗性迁移框架。该方法利用教师模型在仿真数据上的训练优势，通过对抗性学习将长尾场景处理能力迁移至真实世界的学生模型中，从而提升了自动驾驶系统的推理能力和鲁棒性。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>86. Percept-WAM: Perception-Enhanced World-Awareness-Action Model for Robust End-to-End Autonomous Driving</strong><br><span>Jianhua Han, Meng Tian, Jiangtong Zhu, Fan He, Huixin Zhang, Sitong Guo, Dechang Zhu, Hao Tang, Pei Xu, Yuze Guo, Minzhe Niu, Haojie Zhu, Qichao Dong, Xuechao Yan, Siyuan Dong, Lu Hou, Qingqiu Huang, Xiaosong Jia, Hang Xu</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2025-11-24</div><div>2025-11-24</div><div><a href="http://arxiv.org/abs/2511.19221v1">2511.19221v1</a> / <a href="https://arxiv.org/pdf/2511.19221v1">PDF</a></div><div>cs.CV, cs.RO</div></td>
      <td style="width: 10%; vertical-align: top;">VLM</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>自动驾驶在很大程度上依赖于准确且稳健的空间感知。许多失效案例源于感知的不准确和不稳定，特别是在长尾场景和复杂交互中。然而，当前的视觉语言模型（VLM）在空间定位和理解方面较为薄弱，因此构建在这些模型之上的视觉-语言-动作（VLA）系统表现出有限的感知和定位能力。为了应对这些挑战，我们引入了Percept-WAM，这是一个感知增强的世界感知-动作模型。它是首个将2D/3D场景理解能力隐式集成到单个视觉语言模型中的系统。Percept-WAM没有依赖问答式的空间推理，而是通过World-PV和World-BEV标记将2D/3D感知任务统一起来，这些标记同时编码了空间坐标和置信度。我们提出了一种用于密集目标感知的网格条件预测机制，结合了IoU感知评分和并行自回归解码，提升了在长尾、远距离和小目标场景下的稳定性。此外，Percept-WAM利用预训练的VLM参数保留了通用智能（如逻辑推理），并能直接输出感知结果和轨迹控制指令。实验表明，Percept-WAM在下游感知基准测试中匹配或超越了经典的检测器和分割器，在COCO 2D检测和nuScenes BEV 3D检测上分别达到了51.7和58.9的mAP。当与轨迹解码器集成时，它进一步提升了在nuScenes和NAVSIM上的规划性能，例如在NAVSIM上的PMDS指标比DiffusionDrive高出2.1。定性结果进一步突显了其强大的开放词汇表和长尾泛化能力。</td>
      <td style="width: 20%; vertical-align: top;">针对现有视觉语言模型在自动驾驶中空间定位与感知不足的问题，本文提出了Percept-WAM模型。该模型通过引入World-PV和World-BEV标记以及网格条件预测机制，在统一框架内实现了稳健的2D/3D感知与轨迹规划，并在多项基准测试中展现了优于传统方法的感知与规划性能。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>87. Enhancing End-to-End Autonomous Driving with Risk Semantic Distillaion from VLM</strong><br><span>Jack Qin, Zhitao Wang, Yinan Zheng, Keyu Chen, Yang Zhou, Yuanxin Zhong, Siyuan Cheng</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2025-11-18</div><div>2025-11-18</div><div><a href="http://arxiv.org/abs/2511.14499v1">2511.14499v1</a> / <a href="https://arxiv.org/pdf/2511.14499v1">PDF</a></div><div>cs.CV, cs.RO</div></td>
      <td style="width: 10%; vertical-align: top;">VLM, distillation</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>自动驾驶（AD）系统在复杂驾驶场景中表现出色，但泛化能力仍是当前系统的关键瓶颈，特别是在处理未见场景或陌生传感器配置时。相关研究探索了利用视觉语言模型（VLM）来处理少样本或零样本任务。尽管前景广阔，但这些方法引入了新的挑战：产生了一个混合型自动驾驶系统，即使用两个不同的系统来规划轨迹，这可能导致不一致性。其他研究方向探讨了从VLM直接生成控制动作的视觉-语言-动作（VLA）框架，但这些端到端解决方案表现出过高的计算需求。为克服这些挑战，我们引入了风险语义蒸馏（RSD），这是一种利用VLM来增强端到端（E2E）自动驾驶主干网络训练的新型框架。通过为关键对象提供风险关注，RSD解决了泛化问题。具体而言，我们引入了一个名为RiskHead的插件模块，它将视觉语言模型中的因果风险估计蒸馏到鸟瞰图（BEV）特征中，从而产生可解释的风险关注图。这种方法使BEV特征能够学习更丰富、更精细的风险关注表示，直接增强了模型处理空间边界和风险对象的能力。通过专注于风险关注，RSD能更好地与类人驾驶行为对齐，这对在复杂和动态环境中行驶至关重要。我们在Bench2Drive基准测试上的实验证明了RSD在应对复杂和不可预测驾驶条件方面的有效性。由于RSD启用了增强的BEV表示，我们观察到感知和规划能力均得到了显著提升。</td>
      <td style="width: 20%; vertical-align: top;">针对端到端自动驾驶系统在复杂环境下的泛化难题，本文提出了风险语义蒸馏（RSD）框架。该方法通过将视觉语言模型的风险知识蒸馏至BEV特征中，增强了模型对风险对象的关注与空间感知能力。实验表明，该方案在不增加推理计算负担的情况下，显著提升了自动驾驶系统的感知与规划性能。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>88. CorrectAD: A Self-Correcting Agentic System to Improve End-to-end Planning in Autonomous Driving</strong><br><span>Enhui Ma, Lijun Zhou, Tao Tang, Jiahuan Zhang, Junpeng Jiang, Zhan Zhang, Dong Han, Kun Zhan, Xueyang Zhang, XianPeng Lang, Haiyang Sun, Xia Zhou, Di Lin, Kaicheng Yu</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2025-11-17</div><div>2025-11-17</div><div><a href="http://arxiv.org/abs/2511.13297v1">2511.13297v1</a> / <a href="https://arxiv.org/pdf/2511.13297v1">PDF</a></div><div>cs.CV</div></td>
      <td style="width: 10%; vertical-align: top;">world model</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>端到端规划方法是当前自动驾驶系统的既定标准，但由于臭名昭著的长尾问题（即罕见但对安全至关重要的故障案例），数据驱动方法的鲁棒性受到了影响。在这项工作中，我们探讨了最近基于扩散的视频生成方法（即世界模型）与结构化3D布局相结合，是否能够实现一个全自动流程来自我修正此类故障案例。我们首先引入了一个模拟产品经理角色的智能体，称为PM-Agent，它制定数据需求以收集与故障案例相似的数据。然后，我们使用了一个能够模拟数据收集和标注的生成模型。然而，现有的生成模型难以基于3D布局生成高保真的数据。为了解决这个问题，我们提出了DriveSora，它可以生成与PM-Agent请求的3D标注对齐的时空一致视频。我们将这些组件集成到我们的自我修正智能体系统CorrectAD中。重要的是，我们的流程是一个端到端且与模型无关的系统，可以应用于改进任何端到端规划器。在nuScenes和一个更具挑战性的内部数据集上，针对多个端到端规划器进行的评估显示，CorrectAD修正了62.5%和49.8%的故障案例，分别将碰撞率降低了39%和27%。</td>
      <td style="width: 20%; vertical-align: top;">针对自动驾驶端到端规划中的长尾故障问题，本文提出了CorrectAD智能体系统，通过引入PM-Agent制定数据需求并利用DriveSora生成高质量对齐视频来自动修正错误。该方法不依赖于特定模型，通过对故障案例的定向重训练显著降低了碰撞率，提升了端到端规划器的鲁棒性。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>89. Decoupling Scene Perception and Ego Status: A Multi-Context Fusion Approach for Enhanced Generalization in End-to-End Autonomous Driving</strong><br><span>Jiacheng Tang, Mingyue Feng, Jiachao Liu, Yaonong Wang, Jian Pu</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2025-11-17</div><div>2025-11-18</div><div><a href="http://arxiv.org/abs/2511.13079v2">2511.13079v2</a> / <a href="https://arxiv.org/pdf/2511.13079v2">PDF</a></div><div>cs.CV</div></td>
      <td style="width: 10%; vertical-align: top;">distillation</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>面向规划的自动驾驶模块化设计显著推动了端到端系统的发展。然而，现有架构仍然受到对自身状态（ego status）过度依赖的限制，阻碍了泛化能力和稳健的场景理解。我们确定其根本原因在于这些架构中的固有设计，使得自身状态容易被用作捷径。具体而言，在上游 BEV 编码器中过早融合自身状态，导致该强先验信息主导了下游规划模块。为了应对这一挑战，我们提出了 AdaptiveAD，这是一种基于多上下文融合策略的架构级解决方案。其核心是一个明确解耦场景感知与自身状态的双分支结构。一个分支基于多任务学习进行场景驱动推理，但特意在 BEV 编码器中排除了自身状态；另一个分支则仅基于规划任务进行自身驱动推理。随后，一个场景感知融合模块自适应地整合来自两个分支的互补决策，以形成最终的规划轨迹。为确保这种解耦不会损害多任务学习，我们引入了一种用于自身-BEV 交互的路径注意力机制，并增加了两个针对性的辅助任务：BEV 单向蒸馏和自回归在线建图。在 nuScenes 数据集上的广泛评估表明，AdaptiveAD 实现了最先进的开环规划性能。至关重要的是，它显著减轻了对自身状态的过度依赖，并在各种场景中展现了出色的泛化能力。</td>
      <td style="width: 20%; vertical-align: top;">针对端到端自动驾驶中因过度依赖自身状态而导致的泛化瓶颈，本文提出了 AdaptiveAD 架构。该方法通过双分支结构明确解耦场景感知与自身状态，并通过场景感知融合模块与辅助任务机制，显著提升了系统的泛化能力与规划性能。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>90. Prompt-Driven Domain Adaptation for End-to-End Autonomous Driving via In-Context RL</strong><br><span>Aleesha Khurram, Amir Moeini, Shangtong Zhang, Rohan Chandra</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2025-11-16</div><div>2025-11-16</div><div><a href="http://arxiv.org/abs/2511.12755v1">2511.12755v1</a> / <a href="https://arxiv.org/pdf/2511.12755v1">PDF</a></div><div>cs.RO, cs.LG</div></td>
      <td style="width: 10%; vertical-align: top;">VLM, RL</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>尽管自动驾驶领域取得了显著进展，但许多端到端系统在领域自适应（DA）方面仍面临挑战，例如将在晴朗天气下训练的策略迁移到恶劣天气条件下。文献中典型的DA策略包括在目标领域收集额外数据或重新训练模型，甚至两者并举。随着驾驶任务规模和复杂性的增加，这些策略很快变得不切实际。这些局限性促使研究界关注在推理阶段利用大语言模型（LLM）和视觉语言模型（VLM）进行的少样本和零样本提示驱动DA。这些方法通过在推理时向提示词中添加少量状态-动作轨迹（类似于上下文学习）来发挥作用。然而，这种方法存在两个局限性：(i) 目前提示驱动的DA方法仅限于检测和分割等感知任务；(ii) 它们需要专家级的少样本数据。在这项工作中，我们提出了一种新的方法，即利用上下文强化学习（ICRL）在恶劣天气下实现闭环自动驾驶的推理阶段少样本提示驱动DA。与其他提示驱动的DA方法类似，我们的方法不需要更新任何模型参数，也不需要在恶劣天气环境下额外收集数据。此外，我们的方法通过利用推理期间观察到的通用轨迹扩展到闭环驾驶，提升了提示驱动DA的技术水平。我们在CARLA模拟器上的实验表明，与最先进的提示驱动DA基线相比，ICRL在目标领域中实现了更安全、更高效且更舒适的驾驶策略。</td>
      <td style="width: 20%; vertical-align: top;">针对自动驾驶在恶劣天气下领域自适应困难的问题，本文提出了一种基于上下文强化学习（ICRL）的提示驱动方法。该方法无需模型微调或额外数据采集，利用推理时的通用轨迹实现闭环驾驶，实验证明其在安全性和驾驶表现上优于现有的提示驱动基线。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>91. VLA-R: Vision-Language Action Retrieval toward Open-World End-to-End Autonomous Driving</strong><br><span>Hyunki Seong, Seongwoo Moon, Hojin Ahn, Jehun Kang, David Hyunchul Shim</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2025-11-16</div><div>2025-11-16</div><div><a href="http://arxiv.org/abs/2511.12405v1">2511.12405v1</a> / <a href="https://arxiv.org/pdf/2511.12405v1">PDF</a></div><div>cs.CV</div></td>
      <td style="width: 10%; vertical-align: top;">VLM</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>以端到端的方式探索开放世界场景是一项充满前景但也极具挑战的任务，因为它需要强大的泛化能力。特别是在非结构化户外环境下的端到端自动驾驶，经常会遇到训练期间未曾见过的情况。在本文中，我们提出了视觉-语言动作检索（VLA-R），这是一种开放世界端到端自动驾驶（OW-E2EAD）框架，它将开放世界感知与一种新颖的视觉-动作检索范式相结合。我们利用一个冻结的视觉-语言模型进行开放世界检测和分割，无需领域特定微调即可获得多尺度、提示引导且可解释的感知特征。一个 Q-Former 瓶颈层将细粒度的视觉表示与语言对齐的视觉特征进行聚合，从而连接了感知域和动作域。为了学习可迁移的驾驶行为，我们引入了一种视觉-动作对比学习方案，通过对齐视觉-语言嵌入和动作嵌入，实现有效的开放世界推理和动作检索。我们在真实机器人平台上的实验表明，即使在数据有限的情况下，该方法在非结构化且未见过的环境中也表现出强大的泛化能力和探索性能。补充材料中提供了演示视频。</td>
      <td style="width: 20%; vertical-align: top;">针对端到端自动驾驶在开放世界和非结构化环境中面临的泛化难题，本文提出了 VLA-R 框架。该方法结合了冻结视觉-语言模型的感知能力与视觉-动作对比学习，通过动作检索范式实现了在未见环境下的有效驾驶决策。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>92. FLAD: Federated Learning for LLM-based Autonomous Driving in Vehicle-Edge-Cloud Networks</strong><br><span>Tianao Xiang, Mingjian Zhi, Yuanguo Bi, Lin Cai, Yuhao Chen</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2025-11-12</div><div>2025-11-12</div><div><a href="http://arxiv.org/abs/2511.09025v1">2511.09025v1</a> / <a href="https://arxiv.org/pdf/2511.09025v1">PDF</a></div><div>cs.LG</div></td>
      <td style="width: 10%; vertical-align: top;">distillation</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>大型语言模型（LLMs）在自动驾驶（AD）领域展现了出色的数据融合与推理能力。然而，训练用于自动驾驶的LLMs面临着计算传输成本高昂以及敏感驾驶数据隐私担忧等重大挑战。联邦学习（FL）有望使自动驾驶车辆（AVs）能够在不共享原始数据的情况下协同训练模型。我们提出了基于联邦LLM的自动驾驶（FLAD），这是一种利用异构环境中AVs分布式多模态传感器数据的联邦学习框架。FLAD包含三项关键创新：（1）一种云-边-端协同架构，旨在降低通信延迟并保护数据隐私；（2）一种智能并行协同训练机制，包含通信调度算法以优化训练效率，从而利用资源不足的终端设备进行模型训练；（3）一种知识蒸馏方法，可根据异构边缘数据个性化调整LLM。此外，我们在基于NVIDIA Jetson的测试平台上对FLAD进行了原型验证，克服了资源受限设备中的CPU/GPU内存共享、动态模型分区以及容错训练等实际实施挑战。大量的实验评估表明，FLAD在高效利用分布式车载资源的同时，实现了卓越的端到端自动驾驶性能，为未来协作式自动驾驶模型训练与知识共享开辟了新途径。</td>
      <td style="width: 20%; vertical-align: top;">针对自动驾驶中LLM训练面临的资源受限及隐私保护挑战，该论文提出了FLAD框架。该框架采用云-边-端协同架构，通过智能并行调度与知识蒸馏技术，实现了高效的分布式协同训练。实验结果表明，该方法在保障数据隐私的同时，显著提升了资源受限环境下的自动驾驶模型性能。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>93. Constructing the Umwelt: Cognitive Planning through Belief-Intent Co-Evolution</strong><br><span>Shiyao Sang</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2025-10-30</div><div>2026-02-08</div><div><a href="http://arxiv.org/abs/2511.05540v3">2511.05540v3</a> / <a href="https://arxiv.org/pdf/2511.05540v3">PDF</a></div><div>cs.RO, cs.AI, cs.CV, cs.LG, cs.NE</div></td>
      <td style="width: 10%; vertical-align: top;">world model</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>本文挑战了端到端自动驾驶中一个普遍的认识论假设，即高性能规划需要高保真的世界重建。受认知科学启发，我们提出了心理贝叶斯因果世界模型（MBCWM），并将其实现为一种新型认知计算架构：标记化意图世界模型（TIWM）。其核心哲学认为，智能并非源于像素级的客观保真度，而是源于智能体内在的意图世界与物理现实之间的“认知一致性”。通过将冯·尤克斯的“环境（Umwelt）”理论、神经集群假说和三重因果模型（结合符号演绎、概率归纳和力动力学）合成到一个端到端具身规划系统中，我们在nuPlan基准测试上证明了该范式的可行性。开环验证实验结果证实，我们的“信念-意图协同进化”机制有效提升了规划性能。关键在于，在闭环模拟中，该系统展现出了类似人类的突发认知行为，包括对地图可供性的理解、自由探索和自我恢复策略。我们确定认知一致性是核心学习机制：在长期训练过程中，信念（状态理解）和意图（未来预测）通过隐式计算回放自发形成一种自组织平衡，从而实现内在表征与物理世界可供性之间的语义对齐。TIWM为基于重建的规划器提供了一种神经符号化、认知优先的替代方案，确立了一个新的研究方向：将规划视为主动理解而非被动反应。</td>
      <td style="width: 20%; vertical-align: top;">针对端到端自动驾驶中过度依赖高保真世界重建的问题，本文提出了一种基于认知科学的“标记化意图世界模型”（TIWM）。该方法通过信念与意图的协同进化机制建立认知一致性，使系统能够在闭环模拟中展现出主动理解、探索与自适应的类人认知行为。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>94. Alpamayo-R1: Bridging Reasoning and Action Prediction for Generalizable Autonomous Driving in the Long Tail</strong><br><span>NVIDIA, :, Yan Wang, Wenjie Luo, Junjie Bai, Yulong Cao, Tong Che, Ke Chen, Yuxiao Chen, Jenna Diamond, Yifan Ding, Wenhao Ding, Liang Feng, Greg Heinrich, Jack Huang, Peter Karkus, Boyi Li, Pinyi Li, Tsung-Yi Lin, Dongran Liu, Ming-Yu Liu, Langechuan Liu, Zhijian Liu, Jason Lu, Yunxiang Mao, Pavlo Molchanov, Lindsey Pavao, Zhenghao Peng, Mike Ranzinger, Ed Schmerling, Shida Shen, Yunfei Shi, Sarah Tariq, Ran Tian, Tilman Wekel, Xinshuo Weng, Tianjun Xiao, Eric Yang, Xiaodong Yang, Yurong You, Xiaohui Zeng, Wenyuan Zhang, Boris Ivanovic, Marco Pavone</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2025-10-30</div><div>2026-01-07</div><div><a href="http://arxiv.org/abs/2511.00088v2">2511.00088v2</a> / <a href="https://arxiv.org/pdf/2511.00088v2">PDF</a></div><div>cs.RO, cs.AI, cs.LG</div></td>
      <td style="width: 10%; vertical-align: top;">VLM, RL</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>通过模仿学习训练的端到端架构虽然通过扩大模型规模和数据量推动了自动驾驶的发展，但在监督数据稀疏且因果理解有限的安全关键长尾场景中，其性能依然脆弱。我们引入了Alpamayo-R1 (AR1)，这是一种将因果链推理与轨迹规划相结合的视觉-语言-动作模型 (VLA)，适用于复杂的驾驶场景。我们的方法有三个关键创新：(1) 因果链 (CoC) 数据集，通过混合自动标注和人机协同流程构建，生成与驾驶行为对齐的、具有决策依据的因果推理轨迹；(2) 模块化 VLA 架构，结合了为物理人工智能预训练的视觉-语言模型 Cosmos-Reason 和基于扩散的轨迹解码器，能够实时生成动态可行的轨迹；(3) 多阶段训练策略，利用监督微调激发推理能力，并通过强化学习 (RL) 强化推理与动作的一致性并优化推理质量。与纯轨迹基准相比，AR1 在挑战性案例中的规划准确率提高了 12%，在闭环仿真中的近距离接触率降低了 35%。强化学习后训练使推理质量提高了 45%，推理-动作一致性提高了 37%。模型从 0.5B 到 7B 参数的扩展显示出持续的性能提升。车载路测证实了其实时性能（99 毫秒延迟）及城市部署的成功。通过连接可解释的推理与精确控制，AR1 展示了一条通往 L4 级自动驾驶的实践路径。</td>
      <td style="width: 20%; vertical-align: top;">针对自动驾驶在长尾场景下因果理解不足的问题，本文提出了Alpamayo-R1模型，通过引入因果链推理数据集和多阶段训练策略，有效提升了决策的鲁棒性。该方法利用模块化VLA架构实现了推理与轨迹规划的深度融合，显著改善了规划准确率和闭环场景下的安全性。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>95. ZTRS: Zero-Imitation End-to-end Autonomous Driving with Trajectory Scoring</strong><br><span>Zhenxin Li, Wenhao Yao, Zi Wang, Xinglong Sun, Jingde Chen, Nadine Chang, Maying Shen, Jingyu Song, Zuxuan Wu, Shiyi Lan, Jose M. Alvarez</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2025-10-28</div><div>2025-10-28</div><div><a href="http://arxiv.org/abs/2510.24108v1">2510.24108v1</a> / <a href="https://arxiv.org/pdf/2510.24108v1">PDF</a></div><div>cs.RO, cs.CV</div></td>
      <td style="width: 10%; vertical-align: top;">RL</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>端到端自动驾驶将原始传感器输入直接映射为自车轨迹，旨在避免感知模块导致的级联误差并利用丰富的语义线索。现有框架主要依赖模仿学习（IL），其效果常受限于次优的专家示范和部署过程中的协变量偏移。另一方面，强化学习（RL）虽然近期在模拟扩展方面表现出潜力，但通常局限于低维符号输入（如三维物体和地图），难以实现从原始传感器数据进行完全端到端的学习。我们提出了ZTRS（基于轨迹评分的零模仿端到端自动驾驶），一个结合了两方优势的框架：在保留传感器信息的同时利用强化学习进行鲁棒的规划。据我们所知，ZTRS是首个通过仅从奖励中学习，且直接在原始高维传感器数据上运行，从而完全摒弃模仿学习的框架。ZTRS利用离线强化学习以及我们提出的穷举策略优化（EPO），这是一种专为可枚举动作和奖励设计的策略梯度变体。ZTRS在三个基准测试中展现了强劲的性能：Navtest（通用的真实世界开环规划）、Navhard（具挑战性的真实世界和合成场景中的开环规划）以及HUGSIM（模拟闭环驾驶）。具体而言，ZTRS在Navhard上取得了最先进的结果，并在HUGSIM上优于基于模仿学习的基准方法。代码将在https://github.com/woxihuanjiangguo/ZTRS开源。</td>
      <td style="width: 20%; vertical-align: top;">针对端到端自动驾驶中模仿学习依赖专家数据及强化学习难以直接处理高维输入的问题，本文提出了ZTRS框架。该方法引入了穷举策略优化（EPO），实现了在不使用模仿学习的前提下，直接从原始传感器数据进行离线强化学习训练。实验表明，ZTRS在多个驾驶基准测试中优于现有的模仿学习方法，验证了其在复杂场景下的规划性能。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>96. VR-Drive: Viewpoint-Robust End-to-End Driving with Feed-Forward 3D Gaussian Splatting</strong><br><span>Hoonhee Cho, Jae-Young Kang, Giwon Lee, Hyemin Yang, Heejun Park, Seokwoo Jung, Kuk-Jin Yoon</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2025-10-27</div><div>2025-10-27</div><div><a href="http://arxiv.org/abs/2510.23205v1">2510.23205v1</a> / <a href="https://arxiv.org/pdf/2510.23205v1">PDF</a></div><div>cs.CV</div></td>
      <td style="width: 10%; vertical-align: top;">distillation</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>端到端自动驾驶（E2E-AD）作为一种将感知、预测和规划统一到整体数据驱动框架中的新兴范式，展现出巨大潜力。然而，由于车辆配置的多样性，如何实现对不同相机视角的鲁棒性仍是一个尚未解决的难题。为此，我们提出了 VR-Drive，这是一种新型的 E2E-AD 框架，它通过将 3D 场景重建作为辅助任务进行联合学习，从而实现感知规划的视图合成，以解决视角泛化问题。与以往针对特定场景的合成方法不同，VR-Drive 采用前馈推理策略，支持在无需额外标注的情况下进行稀疏视图的在线训练时增强。为了进一步提高视角一致性，我们引入了视角混合记忆库以促进多视角的时序交互，并采用视角一致性蒸馏策略将知识从原始视图迁移到合成视图。VR-Drive 以完全端到端的方式进行训练，有效地减轻了合成引起的噪声，并改善了视角偏移下的规划效果。此外，我们发布了一个新的基准数据集，用于评估 E2E-AD 在新视角下的性能，从而进行全面分析。实验结果表明，VR-Drive 为端到端自动驾驶系统的实际部署提供了一种可扩展且鲁棒的解决方案。</td>
      <td style="width: 20%; vertical-align: top;">针对端到端自动驾驶中不同相机视角导致的鲁棒性不足问题，本文提出了 VR-Drive 框架。该方法通过引入基于前馈 3D 高斯喷溅的辅助场景重建、视角混合记忆库及一致性蒸馏策略，有效提升了系统在视角变化下的规划性能。此外，作者还发布了相关评估数据集以支持该领域的进一步研究。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>97. VGD: Visual Geometry Gaussian Splatting for Feed-Forward Surround-view Driving Reconstruction</strong><br><span>Junhong Lin, Kangli Wang, Shunzhou Wang, Songlin Fan, Ge Li, Wei Gao</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2025-10-22</div><div>2025-10-22</div><div><a href="http://arxiv.org/abs/2510.19578v1">2510.19578v1</a> / <a href="https://arxiv.org/pdf/2510.19578v1">PDF</a></div><div>cs.CV</div></td>
      <td style="width: 10%; vertical-align: top;">distillation</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>前馈式环视自动驾驶场景重建提供了快速且具有泛化能力的推理功能，其核心挑战在于如何在提升新视角质量的同时确保泛化性。由于环视图像重叠区域较少，现有方法通常难以保证新视角的几何一致性和重建质量。为了解决这一矛盾，我们提出必须显式学习几何信息，并利用所得特征来引导提升新视角的语义质量。在本文中，我们引入了“视觉高斯驾驶”（VGD），这是一种为应对上述挑战而设计的新型前馈端到端学习框架。为了实现可泛化的几何估计，我们设计了轻量级的VGGT架构变体，将预训练VGGT的几何先验高效蒸馏到几何分支中。此外，我们设计了一个融合多尺度几何标记的“高斯头”，用于预测新视角渲染的高斯参数，该头部与几何分支共享相同的补丁主干。最后，我们整合了来自几何和高斯头分支的多尺度特征，共同监督语义精炼模型，并通过特征一致性学习优化渲染质量。在nuScenes数据集上的实验表明，我们的方法在多种设置下的客观指标和主观质量方面均显著优于现有最先进的方法，验证了VGD的可扩展性与高保真环视重建能力。</td>
      <td style="width: 20%; vertical-align: top;">针对环视自动驾驶场景中几何一致性和重建质量难以兼顾的问题，本文提出了一种名为VGD的前馈端到端学习框架。通过蒸馏预训练模型的几何先验并设计高斯头，该方法利用多尺度特征实现了高保真的新视角渲染。实验证明，该模型在nuScenes数据集上表现优于当前主流方法，具有良好的泛化能力。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>98. SimpleVSF: VLM-Scoring Fusion for Trajectory Prediction of End-to-End Autonomous Driving</strong><br><span>Peiru Zheng, Yun Zhao, Zhan Gong, Hong Zhu, Shaohua Wu</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2025-10-20</div><div>2025-10-28</div><div><a href="http://arxiv.org/abs/2510.17191v2">2510.17191v2</a> / <a href="https://arxiv.org/pdf/2510.17191v2">PDF</a></div><div>cs.RO, cs.AI</div></td>
      <td style="width: 10%; vertical-align: top;">VLM</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>端到端自动驾驶已成为实现鲁棒且智能驾驶策略的一种有前景的范式。然而，现有的端到端方法仍面临显著挑战，例如在复杂场景下决策欠佳。在本文中，我们提出了 SimpleVSF（一种简单的视觉语言模型评分融合框架），这是一种利用视觉语言模型（VLM）的认知能力和先进轨迹融合技术来增强端到端规划的新型框架。我们使用了传统评分器和新型 VLM 增强型评分器，并利用鲁棒的权重融合器进行定量聚合，以及强大的基于 VLM 的融合器进行定性、上下文感知的决策。作为 ICCV 2025 NAVSIM v2 端到端驾驶挑战赛的领先方法，我们的 SimpleVSF 框架展示了最先进的性能，在安全性、舒适性和效率之间实现了优越的平衡。</td>
      <td style="width: 20%; vertical-align: top;">针对端到端自动驾驶在复杂场景下决策能力不足的问题，本文提出了 SimpleVSF 框架。该方法结合了传统评分器与 VLM 增强评分器，通过权重融合与基于 VLM 的定性融合技术，显著提升了驾驶规划的综合性能，在 ICCV 2025 相关挑战赛中达到了业界领先水平。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>99. Vision-Centric 4D Occupancy Forecasting and Planning via Implicit Residual World Models</strong><br><span>Jianbiao Mei, Yu Yang, Xuemeng Yang, Licheng Wen, Jiajun Lv, Botian Shi, Yong Liu</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2025-10-19</div><div>2026-02-08</div><div><a href="http://arxiv.org/abs/2510.16729v3">2510.16729v3</a> / <a href="https://arxiv.org/pdf/2510.16729v3">PDF</a></div><div>cs.CV</div></td>
      <td style="width: 10%; vertical-align: top;">world model</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>端到端自动驾驶系统越来越依赖以视觉为中心的世界模型来理解和预测其环境。然而，这些模型的一个常见缺陷是对未来场景进行完全重构，这在冗余建模静态背景上浪费了大量能力。为了解决这个问题，我们提出了 IR-WM，这是一种专注于建模当前状态和世界演变的隐式残差世界模型。IR-WM 首先通过视觉观察建立当前状态稳健的鸟瞰图（BEV）表示。然后，它利用前一时间步的 BEV 特征作为强大的时间先验，仅预测“残差”，即基于自车动作和场景上下文的变化。为了减轻随时间推移产生的误差累积，我们进一步应用了一个对齐模块来校准语义和动态的不对齐。此外，我们研究了不同的预测与规划耦合方案，并证明了由世界模型生成的隐式未来状态显著提高了规划精度。在 nuScenes 基准测试中，IR-WM 在 4D 占用预测和轨迹规划方面均取得了顶尖性能。</td>
      <td style="width: 20%; vertical-align: top;">针对现有世界模型在处理静态背景时效率低下的问题，该论文提出了一种隐式残差世界模型（IR-WM），通过仅建模动态变化来提高预测效率。该方法利用时间先验和对齐模块来增强预测的稳健性，并结合隐式未来状态预测提升了自动驾驶轨迹规划的准确性。</td>
    </tr>
    <tr>
      <td style="width: 23%; vertical-align: top;"><strong>100. VDRive: Leveraging Reinforced VLA and Diffusion Policy for End-to-end Autonomous Driving</strong><br><span>Ziang Guo, Zufeng Zhang</span></td>
      <td style="width: 13%; vertical-align: top;"><div>2025-10-17</div><div>2026-02-10</div><div><a href="http://arxiv.org/abs/2510.15446v2">2510.15446v2</a> / <a href="https://arxiv.org/pdf/2510.15446v2">PDF</a></div><div>cs.RO</div></td>
      <td style="width: 10%; vertical-align: top;">RL</td>
      <td style="width: 34%; vertical-align: top;"><strong>中文摘要</strong><br>在自动驾驶中，动态环境和边缘案例对自动驾驶车辆的状态理解和决策稳健性提出了巨大挑战。我们引入了 VDRive，这是一种用于端到端自动驾驶的新型流程，通过显式建模状态-动作映射来应对这些挑战，从而实现可解释且稳健的决策。通过利用视觉语言动作模型 (VLA) 的先进状态理解能力以及基于生成式扩散策略的动作头，VDRive 从情境和几何层面引导驾驶行为。在情境层面，VLA 通过标记生成预训练来预测未来观测，其中观测值由条件向量量化变分自编码器 (CVQ-VAE) 表示为离散代码；在几何层面，我们对 VLA 进行强化学习微调，以根据当前驾驶条件预测未来的轨迹和动作。VLA 为动作策略头提供当前状态标记和预测的状态标记，以生成分层动作和轨迹。在策略训练过程中，学习到的评论家 (critic) 会评估策略生成的动作并提供基于梯度的反馈，从而形成一个支持基于强化学习的策略训练框架的演员-评论家 (actor-critic) 结构。实验表明，VDRive 在 Bench2Drive 闭环基准测试和 nuScenes 开环规划任务中均达到了最先进的性能。</td>
      <td style="width: 20%; vertical-align: top;">针对自动驾驶在动态环境下决策稳健性的难题，本文提出了 VDRive 端到端自动驾驶框架。该方法结合了视觉语言动作模型 (VLA) 的感知能力与扩散策略，并引入强化学习进行微调，实现了更具解释性和鲁棒性的轨迹与动作生成。实验结果证明，该模型在 Bench2Drive 和 nuScenes 等关键基准测试中均展现了领先性能。</td>
    </tr>
  </tbody>
</table>
