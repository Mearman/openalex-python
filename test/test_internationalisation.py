# coding: utf-8

"""
    OpenAlex

    ![](https://raw.githubusercontent.com/ourresearch/openalex-docs/main/.gitbook/assets/OpenAlex-logo-5.png)  **OpenAlex** is a fully open catalog of the global research system.  It's named after the [ancient Library of Alexandria](https://en.wikipedia.org/wiki/Library_of_Alexandria) and made by the nonprofit [OurResearch](https://ourresearch.org/).  ## OpenAPI Specification  [Mearman/openalex-api-spec](https://github.com/Mearman/openalex-api-spec)  This OpenAPI specification is reverse-engineered and derived from spec generated by [openapi-devtools](https://github.com/AndrewWalsh/openapi-devtools).  The specification document itself is OpenAPI version 3.1 and is generated from TypeScript source code.  **[Releases](https://github.com/Mearman/openalex-api-spec/releases)**  ## Clients  [![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=TypeScript&logoColor=white&link=https://github.com/Mearman/openalex-typescript)](https://github.com/Mearman/openalex-typescript)  [![TypeScript Fetch](https://img.shields.io/badge/TypeScript%20Fetch-3178C6?style=for-the-badge&logo=TypeScript&logoColor=white&link=https://github.com/Mearman/openalex-typescript-fetch)](https://github.com/Mearman/openalex-typescript-fetch)  [![TypeScript Node](https://img.shields.io/badge/TypeScript%20Node-339933?style=for-the-badge&logo=Node.js&logoColor=white&link=https://github.com/Mearman/openalex-typescript-node)](https://github.com/Mearman/openalex-typescript-node)  [![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white&link=https://github.com/Mearman/openalex-python)](https://github.com/Mearman/openalex-python) [![Open in](https://img.shields.io/badge/Open%20in-CodeSpaces-181717?style=for-the-badge&logo=GitHub&link=https://codespaces.new/Mearman/openalex-python)](https://codespaces.new/Mearman/openalex-python) [![Open in](https://img.shields.io/badge/Open%20in-Colab-F9AB00?style=for-the-badge&logo=Google%20Colab&link=https://colab.research.google.com/github/Mearman/openalex-python/blob/main/README.ipynb)](https://colab.research.google.com/github/Mearman/openalex-python/blob/main/README.ipynb)  ---

    The version of the OpenAPI document: 0.0.6
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openalex_api.models.internationalisation import Internationalisation

class TestInternationalisation(unittest.TestCase):
    """Internationalisation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Internationalisation:
        """Test Internationalisation
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Internationalisation`
        """
        model = Internationalisation()
        if include_optional:
            return Internationalisation(
                ab = None,
                ace = None,
                aeb_arab = None,
                af = None,
                ak = None,
                alt = None,
                am = None,
                an = None,
                ang = None,
                ar = None,
                arc = None,
                ary = None,
                arz = None,
                var_as = None,
                ast = None,
                atj = None,
                ay = None,
                az = None,
                azb = None,
                ba = None,
                ban = None,
                bar = None,
                bcl = None,
                be = None,
                be_tarask = None,
                bg = None,
                bho = None,
                bi = None,
                bm = None,
                bn = None,
                bo = None,
                bpy = None,
                br = None,
                bs = None,
                bxr = None,
                ca = None,
                cbk_zam = None,
                cdo = None,
                ce = None,
                ceb = None,
                chr = None,
                ckb = None,
                co = None,
                crh = None,
                crh_latn = None,
                cs = None,
                csb = None,
                cv = None,
                cy = None,
                da = None,
                de = None,
                de_at = None,
                de_ch = None,
                diq = None,
                dv = None,
                el = None,
                eml = None,
                en = None,
                en_ca = None,
                en_gb = None,
                en_us = None,
                eo = None,
                es = None,
                et = None,
                eu = None,
                ext = None,
                fa = None,
                fi = None,
                fo = None,
                fr = None,
                frc = None,
                frp = None,
                frr = None,
                fur = None,
                fy = None,
                ga = None,
                gan = None,
                gan_hans = None,
                gan_hant = None,
                gcr = None,
                gd = None,
                gl = None,
                gn = None,
                gpe = None,
                gsw = None,
                gu = None,
                gv = None,
                ha = None,
                hak = None,
                he = None,
                hi = None,
                hif = None,
                hr = None,
                hsb = None,
                ht = None,
                hu = None,
                hy = None,
                hyw = None,
                ia = None,
                id = None,
                ie = None,
                ig = None,
                ilo = None,
                inh = None,
                io = None,
                var_is = None,
                it = None,
                iu = None,
                ja = None,
                jam = None,
                jv = None,
                ka = None,
                kaa = None,
                kab = None,
                kbp = None,
                kg = None,
                kk = None,
                kk_arab = None,
                kk_cn = None,
                kk_cyrl = None,
                kk_kz = None,
                kk_latn = None,
                kk_tr = None,
                kl = None,
                km = None,
                kn = None,
                ko = None,
                ko_kp = None,
                krc = None,
                ks = None,
                ksh = None,
                ku = None,
                ku_latn = None,
                kw = None,
                ky = None,
                la = None,
                lad = None,
                lb = None,
                lfn = None,
                li = None,
                lij = None,
                lld = None,
                lmo = None,
                lo = None,
                lt = None,
                lv = None,
                lzh = None,
                mai = None,
                mg = None,
                min = None,
                mk = None,
                ml = None,
                mn = None,
                mni = None,
                mr = None,
                ms = None,
                ms_arab = None,
                mt = None,
                mwl = None,
                my = None,
                mzn = None,
                nah = None,
                nan = None,
                nap = None,
                nb = None,
                nds = None,
                nds_nl = None,
                ne = None,
                new = None,
                nia = None,
                nl = None,
                nn = None,
                nov = None,
                nqo = None,
                nrm = None,
                oc = None,
                var_or = None,
                os = None,
                pa = None,
                pam = None,
                pap = None,
                pcd = None,
                pdc = None,
                pih = None,
                pl = None,
                pms = None,
                pnb = None,
                ps = None,
                pt = None,
                pt_br = None,
                qu = None,
                rm = None,
                ro = None,
                ru = None,
                rue = None,
                rw = None,
                sa = None,
                sah = None,
                sat = None,
                sc = None,
                scn = None,
                sco = None,
                sd = None,
                se = None,
                sgs = None,
                sh = None,
                shi = None,
                si = None,
                sk = None,
                sl = None,
                smn = None,
                sms = None,
                so = None,
                sq = None,
                sr = None,
                sr_ec = None,
                sr_el = None,
                stq = None,
                su = None,
                sv = None,
                sw = None,
                syl = None,
                szl = None,
                ta = None,
                te = None,
                tg = None,
                tg_latn = None,
                th = None,
                ti = None,
                tk = None,
                tl = None,
                tr = None,
                ts = None,
                tt = None,
                tt_cyrl = None,
                tw = None,
                ug = None,
                uk = None,
                ur = None,
                uz = None,
                vec = None,
                vi = None,
                vls = None,
                vo = None,
                vro = None,
                wa = None,
                war = None,
                wo = None,
                wuu = None,
                xmf = None,
                yi = None,
                yo = None,
                yue = None,
                za = None,
                zh = None,
                zh_cn = None,
                zh_hans = None,
                zh_hant = None,
                zh_hk = None,
                zh_mo = None,
                zh_my = None,
                zh_sg = None,
                zh_tw = None,
                zu = None
            )
        else:
            return Internationalisation(
                en = None,
        )
        """

    def testInternationalisation(self):
        """Test Internationalisation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
