from django.db import models

# Create your models here.


class Cancer(models.Model):
    cancer_name_cn = models.CharField(
        verbose_name='肿瘤中文名', max_length=10, null=True, blank=True)
    cancer_name_en = models.CharField(
        verbose_name='肿瘤英文名', max_length=20, null=True, blank=True)
    category_level_1 = models.CharField(
        verbose_name='等级分类1级', max_length=10, null=True, blank=True)
    category_level_2 = models.CharField(
        verbose_name='等级分类2级', max_length=10, null=True, blank=True)
    category_level_3 = models.CharField(
        verbose_name='等级分类3级', max_length=10, null=True, blank=True)
    category_level_4 = models.CharField(
        verbose_name='等级分类4级', max_length=10, null=True, blank=True)
    category_level_5 = models.CharField(
        verbose_name='等级分类5级', max_length=10, null=True, blank=True)
    category_level_6 = models.CharField(
        verbose_name='等级分类6级', max_length=10, null=True, blank=True)
    heredity_model = models.CharField(
        verbose_name='遗传模型', max_length=20, null=True, blank=True)
    incidence = models.FloatField(verbose_name='发病率', null=True, blank=True)
    mortality = models.FloatField(verbose_name='致死率', null=True, blank=True)
    population_description = models.CharField(
        verbose_name='易患病人群', max_length=100, null=True, blank=True)
    age_choice = models.CharField(
        verbose_name='年龄偏好', max_length=100, null=True, blank=True)
    gender_choice = models.CharField(
        verbose_name='性别偏好', max_length=100, null=True, blank=True)
    symptom = models.TextField(verbose_name='症状', null=True, blank=True)
    cancer_descritpion = models.TextField(
        verbose_name='其它描述', null=True, blank=True)

    class Meta:
        verbose_name = '肿瘤疾病信息'
        verbose_name_plural = '肿瘤疾病信息'


class Panel(models.Model):
    panel_id = models.CharField(
        verbose_name='Panel编号', max_length=10, null=True, blank=True)
    panel_class = models.CharField(
        verbose_name='Panel分类', max_length=20, null=True, blank=True)
    panel_abbr = models.CharField(
        verbose_name='项目简称', max_length=10, null=True, blank=True)
    panel_abbr_pre = models.CharField(
        verbose_name='项目简称-旧', max_length=4, null=True, blank=True)
    panel_name = models.CharField(
        verbose_name='项目名称', max_length=100, null=True, blank=True)
    panel_report_index_name = models.CharField(
        verbose_name='Panel在报告封面的名称', max_length=50, null=True, blank=True)
    panel_report_pageheader_name = models.CharField(
        verbose_name='Panel在报告页眉的名称', max_length=50, null=True, blank=True)
    panel_report_type = models.CharField(
        verbose_name='Panel的报告类型', max_length=10, default='ngs', null=True, blank=True)
    panel_library_method = models.CharField(
        verbose_name='建库方法', max_length=10, null=True, blank=True)
    target_therapy_gene = models.TextField(
        verbose_name='靶向基因', null=True, blank=True)
    chemo_therapy_gene = models.TextField(
        verbose_name='化疗基因', null=True, blank=True)
    genetic_counseling_gene = models.TextField(
        verbose_name='遗传基因', null=True, blank=True)
    immunity_therapy_gene = models.TextField(
        verbose_name='免疫基因', null=True, blank=True)
    mutation_short_gene = models.TextField(
        verbose_name='SNP/Indel基因', null=True, blank=True)
    mutation_cnv_gene = models.TextField(
        verbose_name='CNV基因', null=True, blank=True)
    mutation_fusion_gene = models.TextField(
        verbose_name='融合基因', null=True, blank=True)
    other_gene = models.TextField(verbose_name='其他基因', null=True, blank=True)
    pharmgkb_sites = models.TextField(
        verbose_name='pharmGKB特有位点', null=True, blank=True)

    class Meta:
        verbose_name = 'Panel信息'
        verbose_name_plural = 'Panel信息'


class Gene(models.Model):
    gene_name = models.CharField(
        verbose_name='基因名', max_length=20, null=True, blank=True)
    transcript_id = models.CharField(
        verbose_name='转录本ID', max_length=20, null=True, blank=True)
    transcript_version = models.PositiveSmallIntegerField(
        verbose_name='转录本版本号', null=True, blank=True)
    lrg_number = models.CharField(
        verbose_name='LRG编号', max_length=20, null=True, blank=True)
    gene_alias = models.CharField(
        verbose_name='基因别名', max_length=50, null=True, blank=True)
    gene_description_cn = models.TextField(
        verbose_name='基因中文描述', null=True, blank=True)
    gene_description_en = models.TextField(
        verbose_name='基因英文描述', null=True, blank=True)
    driver_tag = models.BooleanField(
        verbose_name='是否Driver Gene', default=False, null=True, blank=True)
    target_therapy_tag = models.BooleanField(
        verbose_name='是否靶向相关', default=False, null=True, blank=True)
    chemo_therapy_tag = models.BooleanField(
        verbose_name='是否化疗相关', default=False, null=True, blank=True)
    genetic_counseling_tag = models.BooleanField(
        verbose_name='是否遗传相关', default=False, null=True, blank=True)
    immunity_therapy_tag = models.BooleanField(
        verbose_name='是否免疫相关', default=False, null=True, blank=True)

    class Meta:
        verbose_name = 'Gene信息'
        verbose_name_plural = 'Gene信息'


class RefGeneFlat(models.Model):
    gene_name = models.CharField(
        verbose_name='基因名称', max_length=20, null=True, blank=True)
    transcript_id = models.CharField(
        verbose_name='转录本ID', max_length=20, null=True, blank=True)
    chrom = models.CharField(
        verbose_name='染色体', max_length=10, null=True, blank=True)
    strand = models.CharField(
        verbose_name='正负链', max_length=1, null=True, blank=True)
    tx_start = models.PositiveIntegerField(
        verbose_name='起始位置', null=True, blank=True)
    tx_end = models.PositiveIntegerField(
        verbose_name='终止位置', null=True, blank=True)
    cds_start = models.PositiveIntegerField(
        verbose_name='CDS起始位置', null=True, blank=True)
    cds_end = models.PositiveIntegerField(
        verbose_name='CDS终止位置', null=True, blank=True)
    exon_count = models.PositiveSmallIntegerField(
        verbose_name='外显子个数', null=True, blank=True)
    exon_starts = models.TextField(
        verbose_name='各外显子起始位置', null=True, blank=True)
    exon_ends = models.TextField(
        verbose_name='各外显子终止位置', null=True, blank=True)

    class Meta:
        verbose_name = 'RefGene的位置'
        verbose_name_plural = 'RefGene的位置'


class Mutation(models.Model):
    gene_name = models.CharField(
        verbose_name='基因名称', max_length=20, null=True, blank=True)
    mutation_position = models.CharField(
        verbose_name='突变位置描述', max_length=50, null=True, blank=True)
    mutation_hgvs = models.CharField(
        verbose_name='突变HGVS命名', max_length=20, null=True, blank=True)
    driver_tag = models.BooleanField(
        verbose_name='是否Driver突变', default=False, null=True, blank=True)
    benign_tag = models.BooleanField(
        verbose_name='是否良性突变', default=False, null=True, blank=True)
    blacklist_tag = models.BooleanField(
        verbose_name='是否在黑名单中', default=False, null=True, blank=True)
    whitelist_tag = models.BooleanField(
        verbose_name='是否在白名单中', default=False, null=True, blank=True)
    core_panel_only_tag = models.BooleanField(
        verbose_name='是否仅在核心Panel中', default=False, null=True, blank=True)
    BRCA_recheck_tag = models.BooleanField(
        verbose_name='是否需要BRCA校正', default=False, null=True, blank=True)
    mnp_benign_tag = models.BooleanField(
        verbose_name='是否mnp良性突变', default=False, null=True, blank=True)
    panel_abbr_specific = models.CharField(
        verbose_name='针对的Panle简称', max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = '突变信息'
        verbose_name_plural = '突变信息'


class Fusion(models.Model):
    host_gene_name = models.CharField(
        verbose_name='Host基因名', max_length=20, null=True, blank=True)
    partner_gene_name = models.CharField(
        verbose_name='Partner基因名', max_length=20, null=True, blank=True)
    source = models.TextField(verbose_name='信息来源', null=True, blank=True)

    class Meta:
        verbose_name = '融合基因'
        verbose_name_plural = '融合基因'


class OncoKB(models.Model):
    isoform = models.CharField(
        verbose_name='ENST编号', max_length=50, null=True, blank=True)
    refseq = models.CharField(verbose_name='转录本编号',
                              max_length=50, null=True, blank=True)
    entrez_gene_id = models.IntegerField(
        verbose_name='Entrez基因ID', null=True, blank=True)
    gene_name = models.CharField(
        verbose_name='基因名称', max_length=20, null=True, blank=True)
    alteration = models.CharField(
        verbose_name='突变描述', max_length=100, null=True, blank=True)
    protein_change = models.CharField(
        verbose_name='蛋白质变化', max_length=50, null=True, blank=True)
    cancer_type = models.CharField(
        verbose_name='肿瘤类型', max_length=50, null=True, blank=True)
    level = models.CharField(
        verbose_name='等级', max_length=10, null=True, blank=True)
    drug_name = models.CharField(
        verbose_name='药物名称', max_length=100, null=True, blank=True)
    drug_article_pmid = models.TextField(
        verbose_name='药物文章PMID', null=True, blank=True)
    drug_abstract = models.TextField(
        verbose_name='药物描述', null=True, blank=True)

    class Meta:
        verbose_name = 'OncoKB数据库'
        verbose_name_plural = 'OncoKB数据库'


class OncoKBMutation(models.Model):
    isoform = models.CharField(
        verbose_name='ENST编号', max_length=50, null=True, blank=True)
    refseq = models.CharField(verbose_name='转录本编号',
                              max_length=50, null=True, blank=True)
    entrez_gene_id = models.IntegerField(
        verbose_name='Entrez基因ID', null=True, blank=True)
    gene_name = models.CharField(
        verbose_name='基因名称', max_length=20, null=True, blank=True)
    alteration = models.CharField(
        verbose_name='突变描述', max_length=100, null=True, blank=True)
    protein_change = models.CharField(
        verbose_name='蛋白质变化', max_length=50, null=True, blank=True)
    oncogenicity = models.CharField(
        verbose_name='致癌性', max_length=50, null=True, blank=True)
    mutation_effect = models.CharField(
        verbose_name='突变效应', max_length=100, null=True, blank=True)
    mutation_effect_article_pmid = models.TextField(
        verbose_name='突变效应文章PMID', null=True, blank=True)
    mutation_effect_abstract = models.TextField(
        verbose_name='突变效应描述', null=True, blank=True)

    class Meta:
        verbose_name = 'OncoKB数据库Mutation'
        verbose_name_plural = 'OncoKB数据库Mutation'


class Civic(models.Model):
    gene_name = models.CharField(
        verbose_name='基因名称', max_length=20, null=True, blank=True)
    entrez_id = models.PositiveSmallIntegerField(
        verbose_name='Entrez编号', null=True, blank=True)
    variant = models.CharField(
        verbose_name='突变名称-氨基酸变化', max_length=20, null=True, blank=True)
    disease = models.CharField(
        verbose_name='肿瘤类型', max_length=50, null=True, blank=True)
    doid = models.PositiveSmallIntegerField(
        verbose_name='doid', null=True, blank=True)
    phenotypes = models.TextField(verbose_name='表型', null=True, blank=True)
    drugs = models.CharField(
        verbose_name='药物名', max_length=100, null=True, blank=True)
    drug_iteraction_type = models.CharField(
        verbose_name='药物作用类型', max_length=100, null=True, blank=True)
    evidence_type = models.CharField(
        verbose_name='证据类型', max_length=20, null=True, blank=True)
    evidence_direction = models.CharField(
        verbose_name='证据方向', max_length=20, null=True, blank=True)
    evidence_level = models.CharField(
        verbose_name='证据等级', max_length=20, null=True, blank=True)
    clinical_significance = models.CharField(
        verbose_name='临床重要性', max_length=20, null=True, blank=True)
    evidence_statement = models.TextField(
        verbose_name='证据描述', null=True, blank=True)
    citation_id = models.CharField(
        verbose_name='引用的ID', max_length=20, null=True, blank=True)
    source_type = models.CharField(
        verbose_name='引用的源', max_length=20, null=True, blank=True)
    asco_abstract_id = models.CharField(
        verbose_name='ASCO摘要ID', max_length=20, null=True, blank=True)
    citation = models.TextField(verbose_name='引用', null=True, blank=True)
    nct_ids = models.TextField(verbose_name='nct_ids', null=True, blank=True)
    rating = models.PositiveSmallIntegerField(
        verbose_name='Rating', null=True, blank=True)
    evidence_status = models.CharField(
        verbose_name='证据状态', max_length=20, null=True, blank=True)
    evidence_id = models.CharField(
        verbose_name='证据ID', max_length=20, null=True, blank=True)
    variant_id = models.CharField(
        verbose_name='突变ID', max_length=20, null=True, blank=True)
    gene_id = models.CharField(
        verbose_name='基因ID', max_length=20, null=True, blank=True)
    chrom = models.CharField(
        verbose_name='染色体', max_length=10, null=True, blank=True)
    start = models.PositiveIntegerField(
        verbose_name='突变起始位置', null=True, blank=True)
    end = models.PositiveIntegerField(
        verbose_name='突变终止位置', null=True, blank=True)
    reference_base = models.CharField(
        verbose_name='参考碱基', max_length=20, null=True, blank=True)
    variant_base = models.CharField(
        verbose_name='突变碱基', max_length=20, null=True, blank=True)
    representive_transcript = models.CharField(
        verbose_name='ENST编号', max_length=30, null=True, blank=True)
    chrom2 = models.CharField(
        verbose_name='染色体2', max_length=10, null=True, blank=True)
    start2 = models.PositiveIntegerField(
        verbose_name='突变起始位置2', null=True, blank=True)
    end2 = models.PositiveIntegerField(
        verbose_name='突变终止位置2', null=True, blank=True)
    representive_transcript2 = models.CharField(
        verbose_name='ENST编号2', max_length=30, null=True, blank=True)
    ensembl_version = models.CharField(
        verbose_name='ensembl版本', max_length=5, null=True, blank=True)
    reference_build = models.CharField(
        verbose_name='reference版本', max_length=10, null=True, blank=True)
    variant_summary = models.TextField(
        verbose_name='突变统计', null=True, blank=True)
    variant_origin = models.CharField(
        verbose_name='突变来源', max_length=10, default='Somatic', null=True, blank=True)
    last_review = models.DateField(
        verbose_name='review日期', null=True, blank=True)
    evidence_civic_url = models.CharField(
        verbose_name='civic证据链接', max_length=200, null=True, blank=True)
    variant_civic_url = models.CharField(
        verbose_name='civic突变链接', max_length=200, null=True, blank=True)
    gene_civic_url = models.CharField(
        verbose_name='civic基因链接', max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = 'Civic数据库'
        verbose_name_plural = 'Civic数据库'


class PharmGKB(models.Model):
    drug_name = models.CharField(
        verbose_name='药品名称', max_length=50, null=True, blank=True)
    gene_name = models.CharField(
        verbose_name='基因名称', max_length=20, null=True, blank=True)
    rs_id = models.CharField(verbose_name='rs ID',
                             max_length=20, null=True, blank=True)
    geno_type = models.CharField(
        verbose_name='基因型', max_length=50, null=True, blank=True)
    geno_typ_cn = models.CharField(
        verbose_name='基因型中文', max_length=10, null=True, blank=True)
    clinical_type = models.CharField(
        verbose_name='临床类型', max_length=50, null=True, blank=True)
    clinical_guide = models.CharField(
        verbose_name='临床作用', max_length=20, null=True, blank=True)
    evidence = models.CharField(
        verbose_name='证据等级', max_length=4, null=True, blank=True)
    therapeutic_weight = models.IntegerField(
        verbose_name='疗效等级', default=0, null=True, blank=True)
    side_effect_weight = models.IntegerField(
        verbose_name='副作用等级', default=0, null=True, blank=True)
    metabolism = models.CharField(
        verbose_name='代谢等级', max_length=10, null=True, blank=True)
    cds_strand = models.CharField(
        verbose_name='链方向', max_length=10, null=True, blank=True)
    transcript_id = models.CharField(
        verbose_name='转录本ID', max_length=20, null=True, blank=True)
    chrom = models.CharField(
        verbose_name='染色体', max_length=10, null=True, blank=True)
    start = models.PositiveIntegerField(
        verbose_name='起始位置', null=True, blank=True)
    end = models.PositiveIntegerField(
        verbose_name='终止位置', null=True, blank=True)
    pharmgkb_panel = models.TextField(
        verbose_name='pharmGKB Panel', null=True, blank=True)

    class Meta:
        verbose_name = 'PharmGKB数据库'
        verbose_name_plural = 'PharmGKB数据库'


class Hereditary(models.Model):
    gene_name = models.CharField(
        verbose_name='基因名称', max_length=20, null=True, blank=True)
    evidence = models.CharField(
        verbose_name='证据等级', max_length=20, null=True, blank=True)
    risk_level = models.CharField(
        verbose_name='风险等级', max_length=20, null=True, blank=True)
    cancer_type_cn = models.CharField(
        verbose_name='肿瘤类型', max_length=20, null=True, blank=True)
    hereditary_model = models.CharField(
        verbose_name='遗传类型', max_length=20, null=True, blank=True)
    omim_id = models.CharField(
        verbose_name='OMIM ID', max_length=20, null=True, blank=True)
    description = models.TextField(verbose_name='描述', null=True, blank=True)
    disease_description = models.TextField(
        verbose_name='疾病描述', null=True, blank=True)
    tumor_profiles = models.TextField(
        verbose_name='肿瘤profile', null=True, blank=True)

    class Meta:
        verbose_name = '遗传信息'
        verbose_name_plural = '遗传信息'


class ClinicalTrials(models.Model):
    nct_num = models.CharField(
        verbose_name='NCT编号', max_length=20, null=True, blank=True)
    phase = models.CharField(verbose_name='Phase',
                             max_length=20, null=True, blank=True)
    brief_title = models.CharField(
        verbose_name='标题', max_length=20, null=True, blank=True)
    intervention_name = models.CharField(
        verbose_name='干预名称', max_length=20, null=True, blank=True)
    intervention_type = models.CharField(
        verbose_name='干预类型', max_length=20, null=True, blank=True)
    condition = models.CharField(
        verbose_name='适应症', max_length=20, null=True, blank=True)
    country = models.CharField(
        verbose_name='国家', max_length=20, null=True, blank=True)
    overall_status = models.CharField(
        verbose_name='进度', max_length=20, null=True, blank=True)
    study_first_posted = models.DateField(
        verbose_name='发布日期', null=True, blank=True)
    brief_summary = models.TextField(verbose_name='介绍', null=True, blank=True)

    class Meta:
        verbose_name = 'ClinicalTrials数据库'
        verbose_name_plural = 'ClinicalTrials数据库'


class ImmunityReport(models.Model):
    gene_name = models.CharField(
        verbose_name='基因名称', max_length=20, null=True, blank=True)
    clinical_guide = models.TextField(
        verbose_name='临床指导', null=True, blank=True)
    result = models.CharField(
        verbose_name='检测结果', max_length=100, null=True, blank=True)
    effect = models.CharField(
        verbose_name='作用', max_length=20, null=True, blank=True)
    data_info = models.CharField(
        verbose_name='DataInfo', max_length=10, null=True, blank=True)
    panel = models.CharField(verbose_name='Panel',
                             max_length=20, null=True, blank=True)

    class Meta:
        verbose_name = '报告中免疫信息'
        verbose_name_plural = '报告中免疫信息'


class Drug(models.Model):
    drug_name_en = models.CharField(
        verbose_name='药物名-英文', max_length=50, null=True, blank=True)
    drug_name_cn_official = models.CharField(
        verbose_name='药物名-中文-官方', max_length=50, null=True, blank=True)
    drug_name_cn_public = models.CharField(
        verbose_name='药物名-中文-通用', max_length=50, null=True, blank=True)
    drug_name_alias = models.CharField(
        verbose_name='药物名-别名', max_length=50, null=True, blank=True)
    NMPA_approve_tag = models.BooleanField(
        verbose_name='是否NMPA批准', default=False, null=True, blank=True)
    FDA_approve_tag = models.BooleanField(
        verbose_name='是否FDA批准', default=False, null=True, blank=True)
    hormone_tag = models.BooleanField(
        verbose_name='是否激素药物', default=False, null=True, blank=True)
    target = models.CharField(
        verbose_name='药物靶点', max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = '药物信息'
        verbose_name_plural = '药物信息'


class TargetDrug(models.Model):
    drug_generic_name_en = models.CharField(
        verbose_name='英文通用名', max_length=50, null=True, blank=True)
    drug_generic_name_cn = models.CharField(
        '中文通用名', max_length=50, null=True, blank=True)
    common_translation = models.CharField(
        '常用译名', max_length=50, null=True, blank=True)
    brand_name_en = models.CharField(
        '英文商品名', max_length=50, null=True, blank=True)
    brand_name_cn = models.CharField(
        '中文商品名', max_length=50, null=True, blank=True)
    target_drug_tag = models.BooleanField('是否靶向药物', default=True)
    immune_drug_tag = models.BooleanField('是否免疫药物', default=False)
    NMPA_approved_tag = models.BooleanField('是否NMPA批准', default=True)
    NMPA_approved_biomarker = models.CharField(
        'NMPA批准的标志物，对应诊断分类', max_length=50, null=True, blank=True)
    NMPA_approved_usage = models.CharField(
        'NMPA批准的用途', max_length=50, null=True, blank=True)
    NMPA_approved_category = models.CharField(
        'NMPA批准的诊断分类', max_length=50, null=True, blank=True)
    NMPA_offlabel_usage = models.CharField(
        'NMPA超说明书适应症', max_length=50, null=True, blank=True)
    NMPA_offlabel_category = models.CharField(
        'NMPA超说明书诊断分类', max_length=50, null=True, blank=True)
    NMPA_indication = models.CharField(
        'NMPA适应症', max_length=50, null=True, blank=True)
    FDA_approved_tag = models.BooleanField('是否FDA批准', default=True)
    FDA_approved_biomarker = models.CharField(
        'FDA批准的标志物，对应诊断分类', max_length=50, null=True, blank=True)
    FDA_approved_usage_en = models.CharField(
        'FDA批准的用途-英文', max_length=50, null=True, blank=True)
    FDA_approved_usage_cn = models.CharField(
        'FDA批准的用途-中文', max_length=50, null=True, blank=True)
    FDA_approved_category = models.CharField(
        'FDA批准的诊断分类', max_length=50, null=True, blank=True)
    FDA_offlabel_usage_en = models.CharField(
        'FDA超说明书适应症-英文', max_length=50, null=True, blank=True)
    FDA_offlabel_usage_cn = models.CharField(
        'FDA超说明书适应症-中文', max_length=50, null=True, blank=True)
    FDA_offlabel_category = models.CharField(
        'FDA超说明书诊断分类', max_length=50, null=True, blank=True)
    FDA_indication_en = models.CharField(
        'FDA适应症-英文', max_length=50, null=True, blank=True)
    FDA_indication_cn = models.CharField(
        'FDA适应症-中文', max_length=50, null=True, blank=True)
    synonyms = models.CharField('别名', max_length=50, null=True, blank=True)
    pharmacologic_category_en = models.CharField(
        '药理学类别-英文', max_length=50, null=True, blank=True)
    pharmacologic_category_cn = models.CharField(
        '药理学类别-中文', max_length=50, null=True, blank=True)
    dosage_forms_en = models.CharField(
        '剂型-英文', max_length=50, null=True, blank=True)
    dosage_forms_cn = models.CharField(
        '剂型-中文', max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = '靶向药物信息'
        verbose_name_plural = '靶向药物信息'
