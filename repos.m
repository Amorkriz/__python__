%��RGB����ת��Ϊ���еĶ�ά���ֻ꣬ȡ������
function l = repos(r,g,b)
    r = uint16(r);
    g = uint16(g);
    b = uint16(b);
    l = r * 17 * 17 + g * 17 + b;
    
end