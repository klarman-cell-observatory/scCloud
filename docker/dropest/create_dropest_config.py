#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--whitelist')
parser.add_argument('--output')

args = parser.parse_args()
with open(args.output, 'wt') as w:
    w.write('<config>')
    w.write('<Estimation>')
    w.write('<Merge>')
    if args.whitelist is not None:
        w.write('<barcodes_file>{}</barcodes_file>'.format(args.whitelist))
        w.write('<barcodes_type>const</barcodes_type>')
    w.write('<min_merge_fraction>0.2</min_merge_fraction>')
    w.write('<max_cb_merge_edit_distance>2</max_cb_merge_edit_distance>')
    w.write('<max_umi_merge_edit_distance>1</max_umi_merge_edit_distance>')
    w.write('<min_genes_after_merge>100</min_genes_after_merge>')
    w.write('<min_genes_before_merge>20</min_genes_before_merge>')
    w.write('</Merge>')

    w.write('<PreciseMerge>')
    w.write('<max_merge_prob>1e-5</max_merge_prob>')
    w.write('<max_real_merge_prob>1e-7</max_real_merge_prob>')
    w.write('</PreciseMerge>')

    w.write('<BamTags>')
    w.write('<cb>XC</cb>')
    w.write('<umi>XM</umi>')
    w.write('<gene>XG</gene>')
    w.write('<cb_quality>CY</cb_quality>')
    w.write('<umi_quality>UY</umi_quality>')
    w.write('<Type>')
    w.write('<tag>XF</tag>')
    w.write('<intronic>INTRONIC</intronic>')
    w.write('<intergenic>INTERGENIC</intergenic>')
    w.write('</Type>')
    w.write('</BamTags>')
    w.write('</Estimation>')
    w.write('</config>')