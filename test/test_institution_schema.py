# coding: utf-8

"""
    OpenAlex

    ![](https://raw.githubusercontent.com/ourresearch/openalex-docs/main/.gitbook/assets/OpenAlex-logo-5.png)  **OpenAlex** is a fully open catalog of the global research system.  It's named after the [ancient Library of Alexandria](https://en.wikipedia.org/wiki/Library_of_Alexandria) and made by the nonprofit [OurResearch](https://ourresearch.org/).  This OpenAPI specification is derived from spec generated by [openapi-devtools](https://github.com/AndrewWalsh/openapi-devtools).

    The version of the OpenAPI document: 0.0.4-3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from mearman_openalex_api.models.institution_schema import InstitutionSchema

class TestInstitutionSchema(unittest.TestCase):
    """InstitutionSchema unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InstitutionSchema:
        """Test InstitutionSchema
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InstitutionSchema`
        """
        model = InstitutionSchema()
        if include_optional:
            return InstitutionSchema(
                associated_institutions = None,
                cited_by_count = None,
                country_code = None,
                counts_by_year = None,
                created_date = None,
                display_name = None,
                display_name_acronyms = None,
                display_name_alternatives = None,
                geo = mearman_openalex_api.models.geo.geo(
                    city = null, 
                    country = null, 
                    country_code = null, 
                    geonames_city_id = null, 
                    latitude = null, 
                    longitude = null, 
                    region = null, ),
                homepage_url = None,
                id = None,
                ids = mearman_openalex_api.models.ids.ids(
                    crossref = null, 
                    doi = null, 
                    fatcat = null, 
                    grid = null, 
                    issn = null, 
                    issn_l = null, 
                    mag = null, 
                    openalex = null, 
                    orcid = null, 
                    pmcid = null, 
                    pmid = null, 
                    ror = null, 
                    scopus = null, 
                    wikidata = null, 
                    wikipedia = null, ),
                image_thumbnail_url = None,
                image_url = None,
                international = mearman_openalex_api.models.international_display_name.international_display_name(
                    display_name = mearman_openalex_api.models.internationalisation.internationalisation(
                        ab = null, 
                        ace = null, 
                        aeb_arab = null, 
                        af = null, 
                        ak = null, 
                        alt = null, 
                        am = null, 
                        an = null, 
                        ang = null, 
                        ar = null, 
                        arc = null, 
                        ary = null, 
                        arz = null, 
                        as = null, 
                        ast = null, 
                        atj = null, 
                        ay = null, 
                        az = null, 
                        azb = null, 
                        ba = null, 
                        ban = null, 
                        bar = null, 
                        bcl = null, 
                        be = null, 
                        be_tarask = null, 
                        bg = null, 
                        bho = null, 
                        bi = null, 
                        bm = null, 
                        bn = null, 
                        bo = null, 
                        bpy = null, 
                        br = null, 
                        bs = null, 
                        bxr = null, 
                        ca = null, 
                        cbk_zam = null, 
                        cdo = null, 
                        ce = null, 
                        ceb = null, 
                        chr = null, 
                        ckb = null, 
                        co = null, 
                        crh = null, 
                        crh_latn = null, 
                        cs = null, 
                        csb = null, 
                        cv = null, 
                        cy = null, 
                        da = null, 
                        de = null, 
                        de_at = null, 
                        de_ch = null, 
                        diq = null, 
                        dv = null, 
                        el = null, 
                        eml = null, 
                        en = null, 
                        en_ca = null, 
                        en_gb = null, 
                        en_us = null, 
                        eo = null, 
                        es = null, 
                        et = null, 
                        eu = null, 
                        ext = null, 
                        fa = null, 
                        fi = null, 
                        fo = null, 
                        fr = null, 
                        frc = null, 
                        frp = null, 
                        frr = null, 
                        fur = null, 
                        fy = null, 
                        ga = null, 
                        gan = null, 
                        gan_hans = null, 
                        gan_hant = null, 
                        gcr = null, 
                        gd = null, 
                        gl = null, 
                        gn = null, 
                        gpe = null, 
                        gsw = null, 
                        gu = null, 
                        gv = null, 
                        ha = null, 
                        hak = null, 
                        he = null, 
                        hi = null, 
                        hif = null, 
                        hr = null, 
                        hsb = null, 
                        ht = null, 
                        hu = null, 
                        hy = null, 
                        hyw = null, 
                        ia = null, 
                        id = null, 
                        ie = null, 
                        ig = null, 
                        ilo = null, 
                        inh = null, 
                        io = null, 
                        is = null, 
                        it = null, 
                        iu = null, 
                        ja = null, 
                        jam = null, 
                        jv = null, 
                        ka = null, 
                        kaa = null, 
                        kab = null, 
                        kbp = null, 
                        kg = null, 
                        kk = null, 
                        kk_arab = null, 
                        kk_cn = null, 
                        kk_cyrl = null, 
                        kk_kz = null, 
                        kk_latn = null, 
                        kk_tr = null, 
                        kl = null, 
                        km = null, 
                        kn = null, 
                        ko = null, 
                        ko_kp = null, 
                        krc = null, 
                        ks = null, 
                        ksh = null, 
                        ku = null, 
                        ku_latn = null, 
                        kw = null, 
                        ky = null, 
                        la = null, 
                        lad = null, 
                        lb = null, 
                        lfn = null, 
                        li = null, 
                        lij = null, 
                        lld = null, 
                        lmo = null, 
                        lo = null, 
                        lt = null, 
                        lv = null, 
                        lzh = null, 
                        mai = null, 
                        mg = null, 
                        min = null, 
                        mk = null, 
                        ml = null, 
                        mn = null, 
                        mni = null, 
                        mr = null, 
                        ms = null, 
                        ms_arab = null, 
                        mt = null, 
                        mwl = null, 
                        my = null, 
                        mzn = null, 
                        nah = null, 
                        nan = null, 
                        nap = null, 
                        nb = null, 
                        nds = null, 
                        nds_nl = null, 
                        ne = null, 
                        new = null, 
                        nia = null, 
                        nl = null, 
                        nn = null, 
                        nov = null, 
                        nqo = null, 
                        nrm = null, 
                        oc = null, 
                        or = null, 
                        os = null, 
                        pa = null, 
                        pam = null, 
                        pap = null, 
                        pcd = null, 
                        pdc = null, 
                        pih = null, 
                        pl = null, 
                        pms = null, 
                        pnb = null, 
                        ps = null, 
                        pt = null, 
                        pt_br = null, 
                        qu = null, 
                        rm = null, 
                        ro = null, 
                        ru = null, 
                        rue = null, 
                        rw = null, 
                        sa = null, 
                        sah = null, 
                        sat = null, 
                        sc = null, 
                        scn = null, 
                        sco = null, 
                        sd = null, 
                        se = null, 
                        sgs = null, 
                        sh = null, 
                        shi = null, 
                        si = null, 
                        sk = null, 
                        sl = null, 
                        smn = null, 
                        sms = null, 
                        so = null, 
                        sq = null, 
                        sr = null, 
                        sr_ec = null, 
                        sr_el = null, 
                        stq = null, 
                        su = null, 
                        sv = null, 
                        sw = null, 
                        syl = null, 
                        szl = null, 
                        ta = null, 
                        te = null, 
                        tg = null, 
                        tg_latn = null, 
                        th = null, 
                        ti = null, 
                        tk = null, 
                        tl = null, 
                        tr = null, 
                        ts = null, 
                        tt = null, 
                        tt_cyrl = null, 
                        tw = null, 
                        ug = null, 
                        uk = null, 
                        ur = null, 
                        uz = null, 
                        vec = null, 
                        vi = null, 
                        vls = null, 
                        vo = null, 
                        vro = null, 
                        wa = null, 
                        war = null, 
                        wo = null, 
                        wuu = null, 
                        xmf = null, 
                        yi = null, 
                        yo = null, 
                        yue = null, 
                        za = null, 
                        zh = null, 
                        zh_cn = null, 
                        zh_hans = null, 
                        zh_hant = null, 
                        zh_hk = null, 
                        zh_mo = null, 
                        zh_my = null, 
                        zh_sg = null, 
                        zh_tw = null, 
                        zu = null, ), ),
                lineage = None,
                repositories = None,
                roles = None,
                ror = None,
                summary_stats = mearman_openalex_api.models.summary_stats.summary_stats(
                    2yr_mean_citedness = null, 
                    h_index = null, 
                    i10_index = null, ),
                type = None,
                updated_date = None,
                works_api_url = None,
                works_count = None,
                x_concepts = None
            )
        else:
            return InstitutionSchema(
                display_name = None,
                id = None,
        )
        """

    def testInstitutionSchema(self):
        """Test InstitutionSchema"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()